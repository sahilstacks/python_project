from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",password="",database="chatbot_py")
mycursor = db.cursor()
ques = [
    "hello",
    "hi",
    "hey",
    "good morning",
    "good afternoon",
    "good evening",
    "what is your name",
    "who are you",
    "how are you",
    "what is python",
    "what is ai",
    "what is machine learning",
    "what is programming",
    "what is c language",
    "what is java",
    "what is html",
    "what is css",
    "what is javascript",
    "who made you",
    "where are you from",
    "what can you do",
    "tell me a joke",
    "thank you",
    "thanks",
    "bye",
    "goodbye",
    "see you later",
    "how old are you",
    "are you human",
    "what is computer"
]

ans_list = [
    "Hello!",
    "Hello!",
    "Hey!",
    "Good Morning!",
    "Good Afternoon!",
    "Good Evening!",
    "Mera naam AI Bot hai.",
    "Main ek AI chatbot hoon.",
    "Main theek hoon. Aap kaise hain?",
    "Python ek programming language hai.",
    "AI ka matlab Artificial Intelligence hai.",
    "Machine Learning AI ki ek branch hai.",
    "Programming computer ko instructions dene ki process hai.",
    "C ek programming language hai.",
    "Java ek programming language hai.",
    "HTML web pages banane ke liye use hoti hai.",
    "CSS web pages ko design karne ke liye use hoti hai.",
    "JavaScript web pages me interactivity add karti hai.",
    "Mujhe programmers ne banaya hai.",
    "Main computer me rehta hoon.",
    "Main aapke sawalon ke jawab de sakta hoon.",
    "Ek programmer ka favourite place? Cache!",
    "Aapka swagat hai.",
    "Aapka swagat hai.",
    "Alvida!",
    "Goodbye!",
    "Phir milenge!",
    "Main AI hoon, meri age nahi hoti.",
    "Nahi, main AI hoon.",
    "Computer ek electronic machine hai."
]



# Text ko Number me Converter karre hai ham yaha per 
data = CountVectorizer()
x = data.fit_transform(ques)

# AI Model Train Karna ya fir ham yaha per ai model ya brain ko bana rahe hai
bot = MultinomialNB()# ye ek machine learning  alogirithm hai jo ki probablity dekhta hai jo jitne word match hote hai unko check karta hai
bot.fit(x, ans_list)#fit ka matlab model ko train karna ya fir ai model ko sikhana ye ek predefined fucntion hai ml lib ka
print("-----------------------------------------------")
print("    MAYA DEVI UNIVERSITY AI Chatbot Ready")
print("    Band karne ke liye quit likho.\n")
print("-----------------------------------------------")

while True:  #while loop ko maine yaha per infinite kar diya hai
    msg = input("You: ")
    if msg.lower() == "quit":
        print("Bot: Goodbye!")
        break
                     #transform words ko number me convert karraha hai
    user_data = data.transform([msg]) # yaha aap ai ko message pooch rahe ho 
    reply = str(bot.predict(user_data)[0])  # yaha per ai sochta hai answer matlab prediction kar raha hai 

    print("Bot:", reply) #yaha bot answer deta sochke and usko print karde ga

    
    try:
        sql = """INSERT INTO chat_history(user_message, bot_reply)VALUES (%s, %s)"""
        values = (msg, reply)
        mycursor.execute(sql, values)
        db.commit()

    except Exception as e:
        print("Database Error:", e)

mycursor.close()
db.close()
