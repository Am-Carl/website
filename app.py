from flask import Flask, Response

app = Flask(__name__)

@app.route('/.well-known/acme-challenge/IQElqDm11I--IdNx4vWPMRqW9dwKrbZjPFVcECoO7Qk')
def acme_challenge():
    return Response("IQElqDm11I--IdNx4vWPMRqW9dwKrbZjPFVcECoO7Qk.lQEIqDm11I--IdNx4vWPMRqW9dwKrbZjPfVcECoO7Qk.yMGmTZMn6P7FsH8mg127lcPXf7lhddE67VElqiPrLT8", mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)