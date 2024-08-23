

def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'


def classify_temperature_breach(coolingType):
  #lowerLimit = 0
  upperLimit = {
    'PASSIVE_COOLING' : 35,
    'HI_ACTIVE_COOLING' : 45,
    'MED_ACTIVE_COOLING' : 40
  }
  upperLimit = coolingType
  return upperLimit


def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType =\
  lowerLimit = 0
  upperLimit = classify_temperature_breach(batteryChar['coolingType'])
  infer_breach(temperatureInC, lowerLimit, upperLimit)
  if alertTarget == 'TO_CONTROLLER':
    send_to_controller(breachType)
  elif alertTarget == 'TO_EMAIL':
    send_to_email(breachType)


def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')


def send_to_email(breachType):
  recepient = "a.b@c.com"
  if breachType == 'TOO_LOW':
    print(f'To: {recepient}')
    print('Hi, the temperature is too low')
  elif breachType == 'TOO_HIGH':
    print(f'To: {recepient}')
    print('Hi, the temperature is too high')
