from flask import Flask, redirect, request, make_response

app = Flask(__name__)

# Split flag into chunks
flag_parts = ["H&S{", "Ke3P", "-mov1ng", "-4!ways}"]

@app.route("/")
def index():
    # Always redirect to /redirect
    return redirect("/redirect")

@app.route("/redirect")
def loop():
    # Choose a part of the flag based on request count (using query param or fallback)
    # In real deployment, the browser will keep looping, so each redirect will expose a chunk
    step = int(request.args.get("step", 0))

    # Wrap around so it loops infinitely
    part = flag_parts[step % len(flag_parts)]

    # Create response with redirect
    resp = make_response(redirect(f"/redirect?step={(step+1) % len(flag_parts)}"))
    resp.headers["X-File"] = part  # leak flag part in custom header
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
