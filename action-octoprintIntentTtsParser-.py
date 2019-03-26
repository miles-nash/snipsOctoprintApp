#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def intent_received(hermes, intent_message):
    sentence = 'You asked for '

    if intent_message.intent.intent_name == 'overview':
        print('overview')
        sentence += 'an overview of the 3d print'
    elif intent_message.intent.intent_name == 'searchWeatherForecastTemperature':
        print('searchWeatherForecastTemperature')
        sentence += 'the temperature '
    elif intent_message.intent.intent_name == 'searchWeatherForecastCondition':
        print('searchWeatherForecastCondition')
        sentence += 'the weather condition '
    elif intent_message.intent.intent_name == 'searchWeatherForecastItem':
        print('searchWeatherForecastItem')
        sentence += 'the weather '
    else:
        return

   
    hermes.publish_end_session(intent_message.session_id, sentence)


with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
