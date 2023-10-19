rep=True
taux_GBP=0.8759
taux_USD=1.0673
taux_CAD=1.4642

while True:
  print(" ")
  if rep:
    print("Conversion de distances, poids, devises,")
    print("temperature, vitesse, temps, volume, pression")
    print("ou des valeurs numériques.")
    rep=False
  n=int(input("Choisir 1,2,3,4,5,6,7,8 ou 9 : "))
  if n==1:
    print(" ")
    m=int(input("Choisir km → miles (1) ou miles → km (2). "))
    if m==1:
      o=float(input("Choisir la valeur en km : "))
      miles=o/1.609
      print(str(o),"km =",str(round(miles,2)),"mile(s).")
    elif m==2:
      o=float(input("Choisir la valeur en miles : "))
      km=o*1.609
      print(str(o),"miles =",str(round(km,2)),"km.")      
  elif n==2:
    print(" ")
    a=int(input("Choisir kg → lb (1) ou lb → kg (2). "))
    if a==1:
      b=float(input("Choisir la valeur en kg : "))
      lb=b/2.20462
      print(str(b),"kg =",str(round(lb,2)),"lb.")      
    elif a==2:
      b=float(input("Choisir la valeur en lb : "))
      kg=b*2.20462
      print(str(b),"lb =",str(round(kg,2)),"kg.")
  elif n==3:
    print(" ")
    print("Tu peux convertir les euros(EUR) en")
    print("livres(lb), en dollars americains(USD)")
    print("ou en dollars canadiens(CAD).")
    d=int(input("Choisir 1, 2 ou 3. "))
    if d==1:
      c=int(input("Choisir EUR → GBP (1) ou GBP → EUR (2). "))
      if c==1:
        d=float(input("Choisir la valeur en EUR : "))
        GBP=d*taux_GBP
        print(str(d),"EUR =",str(round(GBP,2)),"GBP.")
      elif c==2:
        d=float(input("Choisir la valeur en GBP : "))
        EUR=d/taux_GBP
        print(str(d),"GBP =",str(round(EUR,2)),"EUR.")
    if d==2:
      c=int(input("Choisir EUR → USD (1) ou USD → EUR (2). "))
      if c==1:
        d=float(input("Choisir la valeur en EUR : "))
        USD=d*taux_USD
        print(str(d),"EUR =",str(round(USD,2)),"USD.")
      elif c==2:
        d=float(input("Choisir la valeur en USD : "))
        EUR=d/taux_USD
        print(str(d),"USD =",str(round(EUR,2)),"EUR.")
  elif n==4:
    print(" ")
    c=int(input("Choisir °C → °F (1) ou °F → °C (2) : "))
    if c==1:
      v=int(input("Choisir la valeur en °C : "))
      far=v*9/5+32
      print(str(v),"°C =",str(round(far,2)),"°F.")
    elif c==2:
      v=int(input("Choisir la valeur en °F : "))
      deg=v*9/5+32
      print(str(v),"°F =",str(round(deg,2)),"°C.")
  elif n==5:
    print(" ")
    print("Choisir m/s → km/h (1), km/h → m/s (2),")
    c=int(input("km/h → mph (3) ou mph → km/h (4)  : "))
    if c==1:
      v=int(input("Choisir la valeur en m/s : "))
      kmh=v*3.6
      print(str(v),"m/s =",str(round(kmh,2)),"km/h.")
    elif c==2:
      v=int(input("Choisir la valeur en km/h : "))
      ms=v/3.6
      print(str(v),"km/h =",str(round(ms,2)),"m/s.")
    elif c==3:
      v=int(input("Choisir la valeur en km/h : "))
      mph=v/1.609
      print(str(v),"km/h =",str(round(mph,2)),"mph.")
    elif c==4:
      v=int(input("Choisir la valeur en mph : "))
      kmh=v*1.609
      print(str(v),"mph =",str(round(kmh,2)),"km/h.")
  elif n==6:
    valeurs=["seconde(s)","minute(s)","heure(s)","jour(s)","semaine(s)","mois","année(s)","siècle(s)"]
    print("Tu dois choisir la valeur de départ, qui")
    print("peut être des sec, min, heu, jour,")
    print("semaine, mois, années ou siècles.")
    c=int(input("Choisir 1,2,3,4,5,6,7 ou 8 : "))
    d=int(input("Choisir la valeur de conversion (1,2,3...) : "))
    v=int(input("Combien de",valeurs[c],":"))
    if d==c:
      print("Les deux valeurs sont les mêmes !")
    elif c==1:
      if d==2:
        r=c/60
      elif d==3:
        r=c/3600
      elif d==4:
        r=c/86400
      elif d==5:
        r=c/604800
      elif d==6:
        r=c/2592000
      elif d==7:
        r=c/31104000
      elif d==8:
        r=c/3110400000
    elif c==2:
      if d==1:
        r=c*60
      elif d==3:
        r=c/60
      elif d==4:
        r=c/1440
      elif d==5:
        r=c/10080
      elif d==6:
        r=c/43200
      elif d==7:
        r=c/525600
      elif d==8:
        r=c/52560000
    elif c==3:
      if d==1:
        r=c*3600
      elif d==2:
        r=c*60
      elif d==4:
        r=c/24
      elif d==5:
        r=c/168
      elif d==6:
        r=c/720
      elif d==7:
        r=c/8760
      elif d==8:
        r=c/876000
    elif c==4:
      if d==1:
        r=c*86400
      elif d==2:
        r=c*1440
      elif d==3:
        r=c*24
      elif d==5:
        r=c/7
      elif d==6:
        r=c/30
      elif d==7:
        r=c/365
      elif d==8:
        r=c/36500
    elif c==5:
      if d==1:
        r=c*604800
      elif d==2:
        r=c*10080
      elif d==3:
        r=c*168
      elif d==4:
        r=c*7
      elif d==6:
        r=c/30/7
      elif d==7:
        r=c/52.1429
      elif d==8:
        r=c/5214.29
    elif c==6:
      if d==1:
        r=c*2592000
      elif d==2:
        r=c*43200
      elif d==3:
        r=c*720
      elif d==4:
        r=c*30
      elif d==5:
        r=c*4.29
      elif d==7:
        r=c/12
      elif d==8:
        r=c/1200
    elif c==7:
      if d==1:
        r=c*3153600
      elif d==2:
        r=c*525600
      elif d==3:
        r=c*8760
      elif d==4:
        r=c*365
      elif d==5:
        r=c*52.1429
      elif d==6:
        r=c*12
      elif d==8:
        r=c/100
    elif c==8:
      if d==1:
        r=c*3155760000
      elif d==2:
        r=c*52596000
      elif d==3:
        r=c*876600
      elif d==4:
        r=c*36525
      elif d==5:
        r=c*5218
      elif d==6:
        r=c*1200
      elif d==7:
        r=c*100
    print(str(round(v,2)),valeurs[c],"=",str(round(r,2)),valeurs[d])
  elif n==7:
    print("Il y a m3 → L, m3 → gal ou L → gal.")
    c=int(input("Choisir 1, 2 ou 3 :"))
    if c==1:
      d=int(input("Choisir m3 → L (1) ou L → m3 (2) : "))
      if d==1:
        v=int(input("Choisir la valeur en m3 : "))
        l=v*1000
        print(str(v),"m3 =",str(round(l)),"L.")
      elif d==2:
        v=int(input("Choisir la valeur en L : "))
        met=v/1000
        print(str(v),"L =",str(round(met)),"m3.")
    elif c==2:
      d=int(input("Choisir m3 → gal (1) ou gal → m3 (2) : "))
      if d==1:
        v=int(input("Choisir la valeur en m3 : "))
        gal=v*264.2
        print(str(v),"m3 =",str(round(gal)),"gal.")
      elif d==2:
        v=int(input("Choisir la valeur en gal : "))
        met=v/2964.2
        print(str(v),"gal =",str(round(met)),"m3.")
    elif c==3:
      d=int(input("Choisir m3 → L (1) ou L → m3 (2) : "))
      if d==1:
        v=int(input("Choisir la valeur en gal : "))
        l=v*3.785
        print(str(v),"gal =",str(round(l)),"L.")
      elif d==2:
        v=int(input("Choisir la valeur en L : "))
        gal=v/3.785
        print(str(v),"L =",str(round(gal)),"gal.")
  elif n==8:
    print("Il y a les conversion de Pa → bar, Pa → Psi,")
    print("Pa → mmHg, bar → Psi, bar → mmHg ou Psi → mmHg.")
    c=int(input("Choisir 1, 2, 3, 4, 5 ou 6 : "))
    if c==1:
      r=int(input("Choisr Pa → bar (1) ou bar → Pa (2) : "))
      if r==1:
        v=int(input("Choisir la valeur en Pa : "))
        bar=v/100000
        print(str(v),"Pa =",str(round(bar,2)),"bar.")
      elif r==2:
        v=int(input("Choisir la valeur en bar : "))
        pa=v*100000
        print(str(v),"bar =",str(round(pa,2)),"Pa.")
    elif c==2:
      r=int(input("Choisr Pa → Psi (1) ou Psi → Pa (2) : "))
      if r==1:
        v=int(input("Choisir la valeur en Pa : "))
        psi=v/6895
        print(str(v),"Pa =",str(round(psi,2)),"Psi.")
      elif r==2:
        v=int(input("Choisir la valeur en Psi : "))
        pa=v*6895
        print(str(v),"Psi =",str(round(pa,2)),"Pa.")
    elif c==3:
      r=int(input("Choisr Pa → mmHg (1) ou mmHg → Pa (2) : "))
      if r==1:
        v=int(input("Choisir la valeur en Pa : "))
        mmhg=v/133.3
        print(str(v),"Pa =",str(round(mmhg,2)),"mmHg.")
      elif r==2:
        v=int(input("Choisir la valeur en mmHg : "))
        pa=v*133.3
        print(str(v),"mmHg =",str(round(Pa,2)),"Pa.")
    elif c==4:
      r=int(input("Choisr Psi → bar (1) ou bar → Psi (2) : "))
      if r==1:
        v=int(input("Choisir la valeur en Psi : "))
        bar=v/14.104
        print(str(v),"Psi =",str(round(bar,2)),"bar.")
      elif r==2:
        v=int(input("Choisir la valeur en bar : "))
        psi=v*14.104
        print(str(v),"bar =",str(round(psi,2)),"Psi.")
    elif c==5:
      r=int(input("Choisr mmHg → bar (1) ou bar → mmHg (2) : "))
      if r==1:
        v=int(input("Choisir la valeur en bar : "))
        mmhg=v/750.1
        print(str(v),"bar =",str(round(mmhg,2)),"mmHg.")
      elif r==2:
        v=int(input("Choisir la valeur en mmHg : "))
        bar=v*750.1
        print(str(v),"mmHg =",str(round(bar,2)),"bar.")
    elif c==6:
      r=int(input("Choisr Psi → mmHg (1) ou mmHg → Psi (2) : "))
      if r==1:
        v=int(input("Choisir la valeur en Psi : "))
        mmhg=v*51.715
        print(str(v),"Psi =",str(round(mmhg,2)),"mmHg.")
      elif r==2:
        v=int(input("Choisir la valeur en mmHg : "))
        psi=v/51.715
        print(str(v),"mmHg =",str(round(psi,2)),"Psi.")
  elif n==9:
    print("Il y a dec → hex, dec → bin")
    c=int(input("Choisir 1 ou 2 : "))
    if c==1:
      v=int(input("Choisir la valeur en dec : "))
      hexa=hex(v)
      print(str(v),"=",str(hexa))
    elif c==2:
      v=int(input("Choisir la valeur en dec : "))
      bina=bin(v)
      print(str(v),"=",str(bina))