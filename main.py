import re
import long_responses as long
import telebot


bot = telebot.TeleBot("5939886296:AAE4yWt5-VNikgPLucA7DWTjXUCN-f2Y3jw", parse_mode=None)

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello! Welcome to Vignan group of Institutes.\nHow can i help you?', ['hello', 'hi', 'hey','hlo','hai','namasthe','namaste'],single_response=True)
    response('please feel free to contact me if you require any further information.', ['thankyou','thanks','thank','you'],single_response=True)
    response('The Vignan institutions was established by the Chairman Dr. Lavu Rathaiah,the place with 45 years leagacy of Academic Excellence and Right place for Creative Minds.This is one of the most prestigious and highly-ranked NAAC A+ universities in India. Also, We provide high-quality academic programs, facilitate training and increase industry-institute interactions, and also promoting entrepreneurship, and leadership among students to brighten their future.', ['i', 'need', 'information', 'about','vignan','want','know'], required_words=['vignan'])
    response('Branches in vignan:\nVignan university - Guntur\nVignan\'s LARA Institute of Technology & Science -Guntur\nVignan\'s Nirula Institute of Technology and Science for Women - Guntur\nVignan\'s Institute Of Information Technology - Visakhapatnam\nVignan\'s Institute of Engineering for Womens - Visakhapatnam',['branches','in','vignan'],required_words=['branches','vignan'])
    response('Courses offered:\nB.Tech\nM.Tech\nMBA\nB.Pharm\nMCA', ['about', 'courses','what','are','the','which','vignan'],required_words=['courses'])
    
    # VIEW  -------------------------------------------------------------------------------------------------------
    response('For more details about VIEW you can visit\nhttps://www.view.edu.in/',['details','about','Vignan Institute of Engineering for Women','view','vizag','vishakapatanam','information','info',],required_words=['Vignans Institute of Engineering For Women','details'])
    response('For more details about VIEW you can visit\nhttps://www.view.edu.in/',['details','about','Vignan Institute of Engineering for Women','view','vizag','vishakapatanam','information','info',],required_words=['view','details'])    
    response('https://goo.gl/maps/khziCfEYMgC9Qv2g8',['location','view','Vignan Institute of Engineering for Women'],required_words=['location','view'])
    response('https://goo.gl/maps/khziCfEYMgC9Qv2g8',['location','view','Vignan Institute of Engineering for Women'],required_words=['location','Vignan Institute of Engineering for Women'])
    response('Branches in VIEW are:\nCSE(CS)\nCSE(CC)\nCSE(AI&ML)\nCSE(DS),ECE,EEE,IT,MECH',['branches','departments','streams','in','view','vivp','Vignan Institute of Engineering for Women'],required_words=[' branches','view'])
    response('Branches in VIEW are:\nCSE(CS)\nCSE(CC)\nCSE(AI&ML)\nCSE(DS),ECE,EEE,IT,MECH',['branches','departments','streams','in','view','vivp','Vignan Institute of Engineering for Women'],required_words=['departments','view'])
    
    # VIIT  -------------------------------------------------------------------------------------------------------
    response('For more details about VIIT you can visit\nhttps://vignaniit.edu.in/',['details','about','Vignan Institute of Information & Technology','viit','vizag','vishakapatanam','information','info',],required_words=['Vignans Institute of Information & Technology','details'])
    response('For more details about VIIT you can visit\nhttps://vignaniit.edu.in/',['details','about','Vignan Institute of Information & Technology','viit','vizag','vishakapatanam','information','info',],required_words=['viit','details'])
    response('https://goo.gl/maps/aeQoqNdVnSdpEdkSA',['location','viit','Vignan Institute of Information & Technology'],required_words=['location','viit'])
    response('https://goo.gl/maps/aeQoqNdVnSdpEdkSA',['location','viit','Vignan Institute of Information & Technology'],required_words=['location','Vignan Institute of Information & Technology'])
    response('Branches in VIIT are:\nCivil\nCSE(CS)\nCSE(CC)\nCSE(AI&ML)\nCSE(DS),ECE,EEE,IT,MECH',['branches','departments','streams','in','viit','Vignan Institute of Information & Technology'],required_words=[' branches','viit'])
    response('Branches in VIIT are:\nCivil\nCSE(CS)\nCSE(CC)\nCSE(AI&ML)\nCSE(DS),ECE,EEE,IT,MECH',['branches','departments','streams','in','viit','Vignan Institute of Information & Technology'],required_words=['departments','viit'])
    
    response('CSE,ECE,EEE,Civil,Mech,IT,AI&ML,DS,CC,CS',['about','b.tech','branches','streams','departments','btech','what','are','the','which'],required_words=['btech','branches'])
    response('CSE,ECE,EEE,Civil,Mech,IT,AI&ML,DS,CC,CS',['about','b.tech','branches','streams','departments','btech','what','are','the','which'],required_words=['btech','streams'])
    response('CSE,ECE,EEE,Civil,Mech,IT,AI&ML,DS,CC,CS',['about','b.tech','branches','streams','departments','btech','what','are','the','which'],required_words=['btech','departments'])
    response('CSE,ECE,EEE,Civil,Mech,Aerospace,Biotechnology,Chemical',['about','mtech','branches','streams','what','are','the','which','in'],required_words=['mtech','branches'])
    response('CSE,ECE,EEE,Civil,Mech,Aerospace,Biotechnology,Chemical',['about','mtech','branches','streams','what','are','the','which','in'],required_words=['mtech','streams'])
    response('CSE,ECE,EEE,Civil,Mech,Aerospace,Biotechnology,Chemical',['about','mtech','branches','streams','what','are','the','which','in'],required_words=['mtech','departments'])
    response('HR, Business Management, Marketing, Financial',['about','mba','branches','streams','what','are','the','which','in'],required_words=['mba','branches'])
    response('HR, Business Management, Marketing, Financial',['about','mba','branches','streams','what','are','the','which','in'],required_words=['mba','streams'])
    response('HR, Business Management, Marketing, Financial',['about','mba','branches','streams','what','are','the','which','in'],required_words=['mba','departments'])

    response('Amazon,Accenture,Microsoft,Tech mahindra,Infosys,Intellipaat,TCS,Wipro',['about','offer','placements','companies','company','which','what','are','the'],required_words=['companies'])
    response('We offer campus placements and 90% of students land jobs in MNC\'s',['what','are','the','placements','about'],required_words=['placements'])
    response('Highest packages starts from 44 lpa',['highest','package'],single_response=True)
    response('Lowest package starts from 3 to 4 lpa', ['lowest', 'package'], single_response=True)
    response('our campus is located in a clean,green and spacious region ', ['infrastructure'], single_response=True)
    response('The college offers transportation services to students and faculty coming from different locations',['transport'], single_response=True)
    response('Admissions are based on Entrance exam or Management quota', ['admission'], single_response=True)
    response('eligibility criteria for btech is 10+2 ', ['eligibility','criteria','btech'],required_words=['eligibility','criteria','btech'])
    response('eligibility criteria for mtech is BE/BTECH ', ['eligibility','criteria', 'mtech'],required_words=['eligibility','criteria','mtech'])
    response('eligibility criteria for mba is 10+2+3 ', ['eligibility','criteria', 'mba'],required_words=['eligibility','criteria','mba'])
    response('entrance exams for btech are AP or TS EAMCET', ['entrance','exams','btech'],required_words=['entrance','exam','btech'])
    response('entrance exam for vignan is VSAT', ['entrance','exams','vignan'],required_words=['entrance','exam','vignan'])
    response('entrance exams for mtech are GATE', ['entrance','exams', 'mtech'],required_words=['entrance','exam','mtech'])
    response('entrance exams for mba are ICET', ['entrance','exams', 'mba'],required_words=['entrance','exam','mba'] )
    response('we are required to pay semester fees, lab fees,library fees and building fund yearly', ['fee','structure'], single_response=True)
    response('students who secure seats through counselling are eligibile for fee reimbursement', ['fees','reimbursement'], single_response=True)
    response('students can apply for scholarships depending on their mean and merit', ['scholarship'], single_response=True)
    response('Economically backward students who have  high grade points are eligible for mean scholarship', ['mean','scholarship'],required_words=['mean','scholarship'] )
    response('Students are given merit scholarships based on their academic performance', ['merit scholarship'], single_response=True)
    response('The faculty at Vignan\'s are highly Knowledgeable and qualified,and they instruct the pupils well', ['faculty'], single_response=True)
    response('Every student is given sporting encouragement and make them to participate in National Competitions', ['sports'], single_response=True)
    response('Students are provided with hostel facilities with each room is accomadted with 4 students', ['hostel','facility'],required_words=['hostel','facility'] )
    response('We offer high quality food that is rich in vitamins and proteins', ['hostel','food'], single_response=True)
    response('We have a canteen where all meal options are available,along with all stationary things ', ['canteen'], single_response=True)
    response('We provide laboratories with top-notch,functional equipment,Air conditioning is provided in every '
             'laboratory', ['labs'], single_response=True)
    response('we offer a fantastic library with a wide selection of books for academic purposes, as well as for '
             'several competitve exams and even a digital library', ['library'], single_response=True)
    response('Wifi is available across the campus', ['wifi'], single_response=True)
    response('Teaching techniques used by faculty include chalk and talk,projector and digital', ['teaching','methodology'], single_response=True)
    response('They are different clubs, we host cultural and technical events under these clubs', ['clubs'], single_response=True)
    response('Numerous cultural skills including guitar,dancing and singing are available to students', ['cultural','activites'], single_response=True)
    response('In order to explore the ideas of the students, we conduct hackathon competitions, webinars, and various '
             'curriculum-related activities like essay writing, art, and poetry. ', ['curriculum','activites'], single_response=True)
    response('We organize a fest in which we conduct workshops, a hackathon, food stalls, and cultural events.', ['fests'], single_response=True)
    response('Hostel fees will be around 80k-1l', ['hostel','fees'], required_words=['hostel','fees'])
    response('Hostel fees will be around 80k-1l', ['hostel','fee'], required_words=['hostel','fee'])
    response('Some companies provide internships in addition to placement offers', ['internships'], single_response=True)
    response('We assign mentors to students to help them in all aspects and provide guidance.', ['mentors'], single_response=True)
    response('The students health will be checked once a month and an ambulance is available on site', ['Medical','facility','facilities'],single_response=True)
    response('Campus ragging is not permitted', ['anti','Ragging'], single_response=True)
    response('For more details contact 9133300353', ['contact'], single_response=True)
    response('We provide campus recruitment instruction to the students in order to pick placement candidates.', ['campus','recruitment','training'],single_response=True)
    response('We provide campus recruitment instruction to the students in order to pick placement candidates.', ['crt'],single_response=True)
    response('Students participate in NSS programmes and provide social service by visiting to various locations.', ['nss'], single_response=True)
    response('College hours are from 9:10AM to 4:00PM.', ['what', 'are', 'the','college','timings','clg'], required_words=['timings'])
    response('180 seats are available in CSE', ['how','many','seats','are','available','in','CSE','branch'], required_words=['CSE','seats'])
    response('Students are separated into divisions based on the strength. Every section includes 66 students.', ['how','many','students','are','present','in','each','section'], required_words=['students','section'])
    response('Btech programmes are completed in four years.', ['how','long','it','takes','to','finish','btech','B.tech'], required_words=['B.tech','finish'])
    response('Mtech programmes are completed in two years.', ['how','long','it','takes','to','finish','mtech','M.tech'], required_words=['M.tech','finish'])
    response('RO mineral water is available throughout the college.', ['is', 'water', 'the','college','facility','facilities','available','availibilities'], required_words=['water'])
    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    print(message)
    bot.reply_to(message, get_response(message.text))