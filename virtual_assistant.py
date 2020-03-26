import speech_recognition as sr
def speak(a):
    import os
    
    import pyttsx3

    engine = pyttsx3.init()
    engine.say(a)
    engine.runAndWait()
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        a='hello what you want to do play video in youtube or search wikipedia or gmail'
        speak(a)
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            print('you said',text,' :)')
        except:
            print('we cant recognize you')
        import urllib.request
        import urllib.parse
        import re
        '''print('what you want to do play video in youtube or search wikipedia')
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            print('you said',text,' :)')
        except:
            print('we cant recognize you')'''
        query_string = urllib.parse.urlencode({"search_query" : text})
        print(query_string)
        if('YouTube' in query_string):
            a='what you want to play'
            speak(a)
            audio=r.listen(source)
            try:
                text=r.recognize_google(audio)
                print('you said',text,' :)')
            except:
                print('we cant recognize you')
            query_string = urllib.parse.urlencode({"search_query" : text})
            if('please' in query_string and 'play' in query_string):
                query_string.replace('please','')
                query_string.replace('play','')
                html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
                search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
                import webbrowser
                webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0])
            else:
                print('thank you')
        elif('Wikipedia' in query_string):
            a='what you want to search'
            speak(a)
            audio=r.listen(source)
            try:
                text=r.recognize_google(audio)
                print('you said',text,' :)')
            except:
                print('we cant recognize you')
            query_string = urllib.parse.urlencode({"search_query" : text})
            import wikipedia
            wikipedia.search(query_string)
            ny = wikipedia.page(query_string)
            s=ny.url
            print(s)
            print(ny.title)
            print(ny.content)
            '''html_content = urllib.request.urlopen(s)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            import webbrowser
            webbrowser.open("https://en.wikipedia.org/wiki/" + search_results[0])'''
        elif('Gmail' in query_string):
            a='what you want to send'
            speak(a)
            audio=r.listen(source)
            try:
                text=r.recognize_google(audio)
                print('you said',text,' :)')
            except:
                print('we cant recognize you')
            query_string = urllib.parse.urlencode({"search_query" : text})
            import smtplib as s
            l=s.SMTP('smtp.gmail.com',587)
            l.starttls()
            l.login('enter your mail here','enter your mail password')
            l.sendmail('enter reciever mail',query_string)
            l.close()

listen()
