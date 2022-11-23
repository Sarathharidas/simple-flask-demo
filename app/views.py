from app import app

from flask import request, render_template


@app.route('/')
def hello_world():
  return render_template("index.html")

@app.route('/translate',methods=["GET"])
def downloadFile ():
  #youtube_link =request.args.get('youtube-link')
  #with youtube_dl.YoutubeDL(ydl_opts) as ydl:
      #ydl.download([youtube_link])
  #os.system('whisper "test.wav" --language Hindi --task translate')
  #text_array = []
  #path_name = "test.wav.srt"
  #path_to_download = os.path.abspath(path_name)
  #print("Path",path_to_download)
  #path_to_html = os.path.abspath("index.html")
  #return render_template('index.html')
  # return send_from_directory(os.getcwd(), "content/myfile.txt", as_attachment=True)
  subtitles = open(path_name, "r").read().split("\n\n")
  for i in subtitles:
    text_array+=i.split("\n")
  print(text_array)
  return  render_template("index.html",text=text_array)
    #For windows you need to use drive name [ex: F:/Example.pdf]
    # path =
    # return send_file(path, as_attachment=True)
