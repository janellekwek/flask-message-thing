from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

def retrieve():
    with open("messages.txt", "r") as file:
        total = []
        for line in file:
            split_words = line.split("|")
            total.append({"message": split_words[0], "Author": split_words[0].rstrip()})
    return total

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
         with open("messages.txt", "a") as file:
             file.write(request.form["message"] + "|" + request.form["author"]+ "\n")     
         return redirect(url_for("home"))
    else: # Get request
        total = retrieve()
        return render_template("index.html", messages=total) 

if __name__ == "__main__":
    app.run(debug=True, port=12385)
