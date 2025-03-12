from openai import OpenAI

# Step 1: Initialize the DeepSeek API client
client = OpenAI(api_key="sk-252bfaf9019141e18e453c7460160d8a", base_url="https://api.deepseek.com/v1")


def analyze_article(article_text, analysis_type):
    # Define prompts for each analysis type
    print("1")
    prompts = {
        "5Ws": "Extract the 5Ws (Who, What, When, Where, Why) from the following article:",
        "how": "Explain how the events unfolded in the following article in a short single paragraph:",
    }
    print("2")
    # Prepare the prompt
    prompt = f"{prompts[analysis_type]}\n\n{article_text}"

    print("3")
    # Prepare the messages for the API call
    messages = [{"role": "user", "content": prompt}]

    print("4")
    # Make the API call
    response = client.chat.completions.create(
        model="deepseek-reasoner",  # Use the reasoning model
        messages=messages
    )
    print("5")
    # Extract and return the raw response
    return response.choices[0].message.content

# Function to get separate studies for an article
def get_separate_studies(article_text):
    print("6")
    studies = {}
    studies["5Ws"] = analyze_article(article_text, "5Ws")
    studies["how"] = analyze_article(article_text, "how")
    print("7")
    return studies

# Example usage
if __name__ == "__main__":
    # Article texts (replace with actual article texts)
    article1_text = """ headline: अजित पवार आज कराडमध्ये, राजकीय घडामोडींकडे सगळ्यांचे लक्ष 
    author: 
    story:सातारा जिल्हा हा एकेकाळी राष्ट्रवादी काँग्रेसचा बालेकिल्ला होता. पण आता ती परिस्थिती राहिलेली नाही याची सल अजित पवारांच्या मनामध्ये निश्चितच आहे.
      अजित पवार आज कराडमध्ये, राजकीय घडामोडींकडे सगळ्यांचे लक्ष. दौऱ्यावर असणार आहेत. निमित्त जरी दिवंगत यशवंतराव चव्हाण जयंतीचे असले, काँग्रेसचे 
      नेते अँड.उदयसिंह पाटील यांच्याशी मुंबईत पक्षप्रवेशाबाबत झालेल्या चर्चेनंतर पवार प्रथमच कराड दौऱ्यावर येत असल्याने या दौऱ्यात काय राजकीय घडामोडी होणार? 
      याकडे सर्वांचे लक्ष लागून आहे. दिवंगत यशवंतराव चव्हाण यांची कर्मभूमी म्हणून कराडची ओळख आहे. आधुनिक महाराष्ट्राचे शिल्पकार असणारे यशवंतराव चव्हाण यांच्या 
      कराडला राजकीय पंढरी म्हणूनही ओळखले जाते. प्रत्येक वर्षी पुण्यतिथीला त्यांच्या स्मृतिस्थळी नतमस्तक होण्यासाठी महाराष्ट्रातील राजकीय मंडळीचा मेळा जमतो. पण त्याचबरोबर 
      १२ मार्च च्या जयंतीच्या निमित्ताने अपवाद वगळता प्रत्येक वर्षी नतमस्तक होणारे नेते म्हणजे अजित पवार होत. बुधवारी (१२ मार्च) त्यांचा शासकीय दौरा नुकताच आला असून,
        सकाळी ७:३० वाजता त्यांचे कराडात आगमन होणार आहे. त्यानंतर ते परत मुंबईला जाणार असे नमूद असले तरी तास दोन तासाच्या वेळेत 'कराडच्या पीचवर' ते नेमकी कोणती 
        खेळी करणार? हे पाहणे महत्त्वाचे ठरणार आहे. सातारा जिल्हा हा एकेकाळी राष्ट्रवादी काँग्रेसचा</a> बालेकिल्ला होता. पण आता ती परिस्थिती राहिलेली नाही याची सल 
        अजित पवारांच्या मनामध्ये निश्चितच आहे. म्हणून तर जिल्ह्यात राष्ट्रवादी काँग्रेसची ताकद पुन्हा प्रस्थापित करण्यासाठी त्यांनी वाई- खंडाळ्याला खासदारकी बरोबरच राज्याचे मदत 
        पुनर्वसन मंत्री पदही बहाल केले आहे. त्यामुळे मंत्री मकरंद पाटील व खासदार नितीन पाटील यांच्यावरती जिल्ह्यात पक्ष वाढीची जबाबदारी आहे.
    """
    print("8")
    # Step 1: Get separate studies for both articles
    studies_article1 = get_separate_studies(article1_text)
    print("9")

    # Step 2: Save the raw responses to a file (optional)
    with open("article_responses.json", "w", encoding="utf-8") as f:
        import json
        print("10")
        json.dump({"article1": studies_article1}, f, ensure_ascii=False, indent=4)
    print("11")
      # Step 3: Print the raw responses (for debugging)
    print("Article 1 Studies:", studies_article1)



