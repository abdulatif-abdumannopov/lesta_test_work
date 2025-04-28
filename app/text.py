import math
import re
from collections import Counter
from .models import Document

def process_text(document_instance):
    document_instance.document.open()
    text = document_instance.document.read().decode('utf-8')
    document_instance.document.close()

    words = re.findall(r'\b\w+\b', text.lower())

    tf_counter = Counter(words)

    all_docs = Document.objects.all()
    N = all_docs.count()

    df_counter = Counter()
    total_words = len(words)
    for doc in all_docs:
        doc.document.open()
        doc_text = doc.document.read().decode('utf-8')
        doc.document.close()
        doc_words = set(re.findall(r'\b\w+\b', doc_text.lower()))
        for word in doc_words:
            df_counter[word] += 1

    result = []
    for word, count in tf_counter.items():
        df = df_counter[word]
        idf = math.log(N / df) if df else 0
        result.append({
            'word': word,
            'tf': f"{count / total_words * 100}%",
            'idf': round(idf, 5)
        })

    result = sorted(result, key=lambda x: x['tf'], reverse=True)[:50]
    return result
