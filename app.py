import openai
from Bio import Entrez

openai.api_key = "api"

def get_journal(query, max_results=2):
    Entrez.email = "myemail@gmail.com"
    search_results = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(search_results)
    article_ids = record['IdList']
    
    articles = []
    for article_id in article_ids:
        fetch_handle = Entrez.efetch(db="pubmed", id=article_id, rettype="abstract", retmode="text")
        article_text = fetch_handle.read()
        fetch_handle.close()
        articles.append(article_text)
    return articles

def generate_answer(user_question, selected_article):
    response = openai.Completion.create(
        #engine="text-davinci-003",
        model="gpt-3.5-turbo",
        message=[
            {"role": "user", "content": user_question},
            {"role": "assistant", "content": selected_article}
        ],
        #prompt=f"Context: {context}\n\nQuestion: {prompt}",
        max_tokens=100,
        #n=1,
        #ususstop=None,
        temperature=0.7
    )
    return response['choices'][0]['text'].strip()

def main():
    # Input dari pengguna untuk pertanyaan medis
    user_query = input("Topik Jurnal Medis yang Dicari: ")
    medical_articles = get_journal(user_query)
    if medical_articles:
        print(f"\nDitemukan {len(medical_articles)} artikel dari PubMed")
        for i, article in enumerate(medical_articles, 1):
            print(f"\nArtikel {i}:\n{article[:500]}...")
    else:
        print("Tidak ada artikel yang ditemukan.")
        return
    
    selected_article = medical_articles[0]
    user_question = input("\nPertanyaan terkait artikel 1: ")
    answer = generate_answer(user_question, selected_article)
    
    print(f"\nJawaban:\n{answer}")

if __name__ == "__main__":
    main()