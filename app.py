from flask import Flask, request, redirect, session, render_template, flash

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    # def humiditySensor():
    #     GPIO.setwarnings(True)
    #     GPIO.setmode(GPIO.BCM)
    #     instance = dht11.DHT11(pin=4)
    #     result = instance.read()
    #     if result.is_valid():
    #         data = (str(datetime.datetime.now()), str(result.temperature) + ' ℃', str(result.humidity) + '%')
    #         return data
    #     else:
    #         result = instance.read()
    #         if result.is_valid():
    #             data = (str(datetime.datetime.now()), str(result.temperature) + ' ℃', str(result.humidity) + '%')
    #             return data
    #         else:
    #             if result.is_valid():
    #                 data = (
    #                 str(datetime.datetime.now()), str(result.temperature) + ' ℃', str(result.humidity) + '%')
    #                 return data
    #             else:
    #                 sleep(0.5)
    #                 data = ('no date', 'no temperature', 'no humidity')
    #                 return data
    # return render_template('plants.html', data=humiditySensor(), plants=db['plants'], water=db['water'],
    #                        alan=db['alan'])

    return render_template('main.html')





if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
