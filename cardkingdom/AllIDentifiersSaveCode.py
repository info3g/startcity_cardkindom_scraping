import json
import mysql.connector

f = open('AllIdentifiers.json',"r",encoding='UTF-8')
data = json.loads(f.read())

count=0
for i in data['data']:
	count = count +1
	# print('id:-------',data['data'])
	try:
		artist=data['data'][i]['artist']
	except:
		  artist="Null"
	try:
		availability=data['data'][i]['availability']
	except:
		  availability="Null"
	try:
		borderColor =data['data'][i]['borderColor']
	except:
		  borderColor="Null"
	try:
		colorIdentity =data['data'][i]['colorIdentity']
	except:
		  colorIdentity="Null"
	try:
		colors =data['data'][i]['colors']
	except:
		  colors="Null"
	try:
		convertedManaCost =data['data'][i]['convertedManaCost']
	except:
		  convertedManaCost="Null"
	try:
		edhrecRank =data['data'][i]['edhrecRank']
	except:
		  edhrecRank="Null"
	try:
		finishes =data['data'][i]['finishes']
	except:
		  finishes="Null"
	try:
		flavorText =data['data'][i]['flavorText']
	except:
		  flavorText="Null"
	try:
		for x in data['data'][i]['foreignData']:
			try:
				flavorTexts =x['flavorText']
			except:
				flavorTexts="Null"
			try:
				language =x['language']
			except:
				language="Null"
			try:
				multiverseId =x['multiverseId']
			except:
				multiverseId="Null"
			try:
				names =x['name']
			except:
				names="Null"
			try:
				texts =x['text']
			except:
				texts="Null"
			try:
				type =x['type']
			except:
				type="Null"
	except:
		pass
	 
	try:
		frameVersion =data['data'][i]['frameVersion']
	except:
		frameVersion="Null"
	try:
		hasFoil =data['data'][i]['hasFoil']
	except:
		hasFoil="Null"
	try:
		hasNonFoil =data['data'][i]['hasNonFoil']
	except:
		hasNonFoil="Null"
	try:
		cardKingdomFoilId =data['data'][i]['identifiers']['cardKingdomFoilId']
	except:
		cardKingdomFoilId="Null"
	try:
		mcmId =data['data'][i]['identifiers']['mcmId']
	except:
		mcmId="Null"
	try:
		mtgjsonV4Id =data['data'][i]['identifiers']['mtgjsonV4Id']
	except:
		mtgjsonV4Id="Null"
	try:
		scryfallId =data['data'][i]['identifiers']['scryfallId']
	except:
		scryfallId="Null"
	try:
		scryfallIllustrationId =data['data'][i]['identifiers']['scryfallIllustrationId']
	except:
		scryfallIllustrationId="Null"
	try:
		scryfallOracleId =data['data'][i]['identifiers']['scryfallOracleId']
	except:
		scryfallOracleId="Null"
	try:
		tcgplayerProductId =data['data'][i]['identifiers']['tcgplayerProductId']
	except:
		tcgplayerProductId="Null"
	try:
		isPromo =data['data'][i]['isPromo']
	except:
		isPromo="Null"
	try:
		isReprint =data['data'][i]['isReprint']
	except:
		isReprint="Null"
	try:
		isStarter =data['data'][i]['isStarter']
	except:
		isStarter="Null"
	try:
		keywords =data['data'][i]['keywords']
	except:
		keywords="Null"
	try:
		layout =data['data'][i]['layout']
	except:
		layout="Null"
	try:
		legalities_commander =data['data'][i]['legalities']['commander']
	except:
		legalities_commander="Null"
	try:
		legalities_duel =data['data'][i]['legalities']['duel']
	except:
		legalities_duel="Null"
	try:
		legalities_legacy =data['data'][i]['legalities']['legacy']
	except:
		legalities_legacy="Null"
	try:
		legalities_modern =data['data'][i]['legalities']['modern']
	except:
		legalities_modern="Null"
	try:
		legalities_penny =data['data'][i]['legalities']['penny']
	except:
		legalities_penny="Null"
	try:
		legalities_pioneer =data['data'][i]['legalities']['pioneer']
	except:
		legalities_pioneer="Null"
	try:
		legalities_vintage =data['data'][i]['legalities']['vintage']
	except:
		legalities_vintage="Null"
	try:
		manaCost =data['data'][i]['manaCost']
	except:
		manaCost="Null"
	try:
		manaValue =data['data'][i]['manaValue']
	except:
		manaValue="Null"
	try:
		name =data['data'][i]['name']
	except:
		name="Null"
	try:
		numbers =data['data'][i]['number']
	except:
		numbers="Null"
	try:
		power =data['data'][i]['power']
	except:
		power="Null"
	try:
		printings =data['data'][i]['printings']
	except:
		printings="Null"
	try:
		promoTypes =data['data'][i]['promoTypes']
	except:
		promoTypes="Null"
	try:
		cardKingdomFoil =data['data'][i]['purchaseUrls']['cardKingdomFoil']
	except:
		cardKingdomFoil="Null"
	try:
		tcgplayer =data['data'][i]['purchaseUrls']['tcgplayer']
	except:
		tcgplayer="Null"
	try:
		rarity =data['data'][i]['rarity']
	except:
		rarity="Null"
	try:
		for j in data['data'][i]['rulings']:
			try:
				dates =j['date']
			except:
				dates="Null"
			try:
				textt =j['text']
			except:
				textt="Null"
	except:
		pass
	try:
		securityStamp =data['data'][i]['securityStamp']
	except:
		securityStamp="Null"
	try:
		setCode =data['data'][i]['setCode']
	except:
		setCode="Null"
	try:
		subtypes =data['data'][i]['subtypes']
	except:
		subtypes="Null"
	try:
		supertypes =data['data'][i]['supertypes']
	except:
		supertypes="Null"
	try:
		textss =data['data'][i]['text']
	except:
		textss="Null"
	try:
		toughness =data['data'][i]['toughness']
	except:
		toughness="Null"
	try:
		typess =data['data'][i]['type']
	except:
		typess="Null"
	try:
		types =data['data'][i]['types']
	except:
		types="Null"
	try:
		uuid =data['data'][i]['uuid']
	except:
		uuid="Null"
	print(".....................-----------------------",count)
	kwargs = {'uuid': str(uuid)}
    where_clause = 'WHERE ' + ' AND '.join([' ' + k + ' = %s' for k in kwargs.keys()])
    values = tuple(kwargs.values())
    sql = "SELECT *  FROM cardkingdom " + where_clause
    mycursor.execute(sql, values)
    myresult = mycursor.fetchall()
    print("myresultmyresultmyresult",len(myresult),myresult)
    if len(myresult)==0:
		connection = mysql.connector.connect(host="localhost",user="root",password="",database='test')
		mycursor = connection.cursor(buffered=True)
		sql = '''INSERT INTO cardkingdom (artist ,availability,colorIdentity,colors ,convertedManaCost,finishes,flavorText,hasFoil,hasNonFoil,isPromo,isReprint,isStarter,keywords,layout,legalities_commander,legalities_duel,legalities_legacy,legalities_modern,legalities_penny,legalities_pioneer,legalities_vintage,manaCost,manaValue,name,numbers,power,printings,promoTypes,rarity,setCode,subtypes,supertypes,textss,toughness,typess,types,uuid) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
		val = (str(artist) ,str(availability),str(colorIdentity),str(colors) ,str(convertedManaCost),str(finishes),str(flavorText),str(hasFoil),str(hasNonFoil),str(isPromo),str(isReprint),str(isStarter),str(keywords),str(layout),str(legalities_commander),str(legalities_duel),str(legalities_legacy),str(legalities_modern),str(legalities_penny),str(legalities_pioneer),str(legalities_vintage),str(manaCost),str(manaValue),str(name),str(numbers),str(power),str(printings),str(promoTypes),str(rarity),str(setCode),str(subtypes),str(supertypes),str(textss),str(toughness),str(typess),str(types),str(uuid) )
		mycursor.execute(sql,val)
		connection.commit()

	if count == 100:
		break
 