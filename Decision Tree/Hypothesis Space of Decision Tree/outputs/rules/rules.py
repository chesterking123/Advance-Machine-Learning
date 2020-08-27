def findDecision(obj): #obj[0]: Day, obj[1]: Outlook, obj[2]: Temperature, obj[3]: Humidity, obj[4]:  Wind
   if obj[0] == 'D6':
      return 'No '
   elif obj[0] == 'D1':
      return 'No '
   elif obj[0] == 'D8':
      return 'No '
   elif obj[0] == 'D13':
      return 'Yes '
   elif obj[0] == 'D2':
      return 'No '
   elif obj[0] == 'D3':
      return 'Yes '
   elif obj[0] == 'D5':
      return 'Yes '
   elif obj[0] == 'D9':
      return 'Yes '
   elif obj[0] == 'D7':
      return 'Yes '
   elif obj[0] == 'D14':
      return 'No'
   elif obj[0] == 'D10':
      return 'Yes '
   elif obj[0] == 'D4':
      return 'Yes'
   elif obj[0] == 'D12':
      return 'Yes '
   elif obj[0] == 'D11':
      return 'Yes '
   else:
      return 'Yes '
