import streamlit as st

import os
import google.generativeai as genai

st.set_page_config(page_title=" Trip planner App")
st.title(' plan your trip')

openai_api_key = st.sidebar.text_input('gemini API Key')



def initiatemodel(openai_api_key):
    genai.configure(api_key=openai_api_key)

    # Create the model
    # See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        # safety_settings = Adjust safety settings
        # See https://ai.google.dev/gemini-api/docs/safety-settings
        system_instruction="You are an Indian travel guide and have a lot of experience leading a trip  with lot of people\\nand also have an idea to fit budget trip frugally with attention to detailou are an Indian travel guide and have a lot of experience leading a trip  with lot of people and also have an idea to fit budget trip frugally with attention to detailSuggest me some good 4-5 star hotels and resorts in Bali I can stay in. Make sure to keep my itinerary in mind and ensure it’s not too far from the things I want to do. Also, include a rough price estimate for each hotel Suggest me quick and affordable trains to get to kerala from hyderabad, India . Include the names of the train express, how long they will take, and also add a rough estimate of how much each will cost.With all the information I have selected, create two different tables summarising my final itinerary in detail, the entire budget, emergency numbers, customs, and safety. Keep the customs and safety brief.",
    )

    return model


def generate_response(input_text):
    llm = initiatemodel(openai_api_key)
    chat_session = llm.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    "Can you help me with an 5 day trip iternary for  kerala trip starting from Hyderabad ",
                    "Can you help me with an 5 day trip iternary for  kerala trip starting from Hyderabad ",
                ],
            },
            {
                "role": "model",
                "parts": [
                    "Okay! Let's create a beautiful 5-day itinerary for your Kerala trip, starting from Hyderabad. This itinerary focuses on the classic Kerala experience, combining stunning scenery, cultural immersion, and relaxation. \n\n**Day 1: Hyderabad to Kochi (via Flight) – Explore Fort Kochi**\n\n* Morning: Fly from Hyderabad to Kochi (approx. 2 hours).\n* Afternoon: Check into your hotel in Fort Kochi.  \n* Evening: Explore Fort Kochi's historic streets:\n    * Visit St. Francis Church (the oldest European church in India).\n    * Wander through the Jewish Quarter and see the Paradesi Synagogue.\n    * Enjoy the vibrant atmosphere of the Chinese Fishing Nets.\n* Dinner: Savor a delicious Kerala meal at a local restaurant, enjoying traditional dishes like Appam and Stew.\n\n**Day 2: Backwaters and Houseboat Experience**\n\n* Morning: Enjoy a delicious South Indian breakfast at your hotel.\n* Morning: Take a ferry from Fort Kochi to Alleppey (approx. 1 hour).\n* Afternoon: Check into a traditional Kerala houseboat (Kettuvallam) at Alleppey.\n* Afternoon/Evening: Cruise through the serene backwaters, taking in the lush landscapes, local villages, and the unique birdlife.  Enjoy a delicious Kerala lunch and dinner prepared on the houseboat.\n\n**Day 3:  Munnar - Hill Station Charm**\n\n* Morning:  Enjoy a leisurely breakfast on the houseboat. \n* Morning:  Check out of the houseboat and take a taxi from Alleppey to Munnar (approx. 4 hours).\n* Afternoon: Check into your hotel in Munnar and relax.\n* Evening:  Explore Munnar's tea plantations:\n    * Visit a tea factory for a guided tour to learn about tea production.\n    * Take a walk through the lush green hills and enjoy the panoramic views.\n    * Enjoy a cup of fresh tea at one of the many tea estates.\n* Dinner:  Enjoy a delicious dinner at a restaurant in Munnar.\n\n**Day 4:  Munnar's Natural Wonders**\n\n* Morning:  Enjoy a leisurely breakfast at your hotel.\n* Morning: Visit Mattupetty Dam:\n    * Enjoy boat rides on the serene lake.\n    *  Take a walk around the dam and enjoy the beautiful scenery. \n* Afternoon:  Explore Eravikulam National Park:\n    *  See the endangered Nilgiri Tahr.\n    *  Take a scenic hike through the park's diverse flora and fauna.\n* Evening:  Enjoy a relaxing evening in Munnar.\n\n**Day 5:  Return to Hyderabad**\n\n* Morning:  Enjoy a leisurely breakfast at your hotel.\n* Morning:  Take a taxi from Munnar to Kochi Airport (approx. 3.5 hours).\n* Afternoon: Fly back to Hyderabad from Kochi.\n\n**Tips for your Trip**\n\n* **Season:** The best time to visit Kerala is between October and May.\n* **Transportation:** Pre-book taxis or use ride-sharing services for transfers. \n* **Kerala Cuisine:**  Enjoy Kerala's unique dishes like Appam, Puttu, and Fish Curry. \n* **Accommodation:** Book accommodations in advance, especially during peak season.\n* **Cultural Experiences:**  Participate in traditional Kerala dance performances (Kathakali) or witness the vibrant Thrissur Pooram festival (if you're visiting during April/May).\n* **Safety:**  Stay aware of your surroundings and be mindful of your belongings.\n* **Clothing:** Pack comfortable clothing, as you will be doing a lot of walking and exploring.\n\n**Additional Options:**\n\n* If you have more time, you could include a visit to Thekkady, known for its Periyar Wildlife Sanctuary and spice plantations.\n* You can also explore the coastal towns of Kovalam and Varkala for their beaches and Ayurvedic treatments.\n\nI hope this itinerary helps you plan your dream Kerala trip! Remember to always be flexible and open to new experiences. Enjoy your journey! \n",
                ],
            },
            {
                "role": "user",
                "parts": [
                    "what is the best time to visit kerala\n",
                ],
            },
            {
                "role": "model",
                "parts": [
                    "You're right to ask about the best time to visit Kerala! It really depends on what kind of experience you're looking for. Here's a breakdown of the seasons and what they offer:\n\n**Peak Season (October - May):**\n\n* **Weather:** Generally sunny, warm, and dry. Perfect for outdoor activities, exploring, and enjoying Kerala's natural beauty.\n* **Pros:**  Pleasant temperatures, clear skies, less rainfall, ideal for exploring backwaters, beaches, and hill stations.\n* **Cons:**  More crowded, higher prices for accommodations and tours.\n\n**Monsoon Season (June - September):**\n\n* **Weather:**  Heavy rainfall, lush greenery, cooler temperatures.\n* **Pros:**  The landscape is incredibly green and vibrant.  Backwaters are overflowing, creating an even more picturesque experience. \n* **Cons:**  Heavy rainfall can disrupt travel plans and some outdoor activities may be limited.\n\n**Specific Time Recommendations:**\n\n* **October to March:** Ideal for enjoying the best of Kerala's weather and a wide range of activities. \n* **April/May:**  If you want to experience the vibrant Thrissur Pooram festival (a grand Hindu temple festival) - but it's very hot.\n* **June to September:**  Perfect for experiencing the monsoon magic, but be prepared for rain.\n\n**Consider this:**\n\n* **Backwaters:**  The best time to experience the backwaters is during the monsoon season (June to September), but keep in mind the potential for rain.\n* **Hill Stations:**  The cooler months (October to March) are ideal for exploring Munnar and other hill stations.\n* **Beaches:**  The winter months (October to March) offer the best weather for enjoying the beaches. \n\n**My Recommendation:**\n\nFor a balanced experience,  **October to March** is generally the best time to visit Kerala. You'll enjoy pleasant weather, vibrant landscapes, and a wide range of activities.  If you're up for a bit of adventure and don't mind the rain, the monsoon season (June to September) can offer a unique and breathtaking experience. \n\nLet me know if you have any other questions about your Kerala trip! I'm happy to help!\n",
                ],
            },
            {
                "role": "user",
                "parts": [
                    "trip to kerala\n",
                ],
            },
            {
                "role": "model",
                "parts": [
                    "Okay, let's plan your Kerala trip!  To give you the best suggestions, please tell me a bit more about what you're looking for:\n\n**1. What are your main interests?**\n\n* **Relaxation:**  Beaches, backwaters, Ayurvedic treatments\n* **Adventure:**  Trekking, wildlife safaris, water sports\n* **Culture:**  Temples, festivals, traditional dance, local cuisine\n* **History:**  Fort Kochi, colonial architecture, historical sites\n\n**2.  What is your budget?**\n\n* This will help me suggest accommodations and activities that fit your budget.\n\n**3.  What dates are you looking to travel?**\n\n*  Knowing your dates will help me suggest the best time to visit based on the weather and festivals.\n\n**4.  How many people are travelling?**\n\n*  This will impact transportation and accommodation choices.\n\n**5.  What type of accommodation are you looking for?**\n\n*  Luxury resorts, budget-friendly homestays, charming boutique hotels?\n\nOnce I have this information, I can create a detailed itinerary, including:\n\n* **Flights and transportation**\n* **Accommodation recommendations**\n* **Activities and attractions**\n* **Food and dining suggestions**\n* **Travel tips and safety advice**\n\nI'm excited to help you plan your Kerala adventure! \n",
                ],
            },
        ]
    )
    response = chat_session.send_message(input_text)

    st.info(response.text)


with st.form('my_form'):
    text = st.text_area('Enter text:', 'Plan a 3 day trip to kerala')
    Destination = st.text_area('Enter Destination:', 'Goa')
    days = st.number_input("No of days:",step=1,value=1)
    travelstyle = st.radio(
        "Travel Style",
        ["budget friendly ", "***luxury***"],
        index=0,
    )

    interests = st.selectbox(
        "What are your Interests ?",
        ("beaches", " back waters ", "culture","party"))

    startPoint = st.text_area('Enter startPoint:', 'Hyderabad ')

    submitted = st.form_submit_button('Submit')

    if submitted:
        generate_response(text)
