from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


events = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title")
        date = request.form.get("date")
        time = request.form.get("time")
        priority = request.form.get("priority")

        if title:  
            events.append({
                "id": len(events),
                "title": title,
                "date": date,
                "time": time,
                "priority": priority
            })

        return redirect(url_for("index"))

    return render_template("index.html", events=events)


@app.route("/delete/<int:event_id>")
def delete(event_id):
    global events
    events = [event for event in events if event["id"] != event_id]


    for i, event in enumerate(events):
        event["id"] = i

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)