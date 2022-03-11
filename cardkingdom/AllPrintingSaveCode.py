import json
import time
import mysql.connector
f = open('AllPrintings.json',"r",encoding='UTF-8')
data = json.loads(f.read())
# print(data['data'])
count=0
for i in data['data']:
	count=count+1
	time.sleep(5)
	for x in data['data'][i]['cards']:
		try:
			artist=x['artist']
			# print(artist)
		except:
			artist="Null"
		try:
		   availability=x['availability']
		except:
			availability="Null"
		try:
		   borderColor =x['borderColor']
		except:
			borderColor="Null"
		try:
		   colorIdentity =x['colorIdentity']
		except:
			colorIdentity="Null"
		try:
		   colors =x['colors']
		except:
			colors="Null"
		try:
		   convertedManaCost =x['convertedManaCost']
		except:
			convertedManaCost="Null"
		try:
			edhrecRank =x['edhrecRank']
		except:
			edhrecRank="Null"
		try:
			finishes =x['finishes']
		except:
			finishes="Null"
		try:
			flavorText =x['flavorText']
		except:
			flavorText="Null"
		try:
			for j in x['foreignData']:
				try:
					flavorTexts =j['flavorText']
				except:
					flavorTexts="Null"
				try:
					language =j['language']
				except:
					language="Null"
				try:
					multiverseId =j['multiverseId']
				except:
					multiverseId="Null"
				try:
					names =j['name']
				except:
					names="Null"
				try:
					texts =j['text']
				except:
					texts="Null"
				try:
					type =j['type']
				except:
					type="Null"
		except:
			pass
		try:
			frameVersion =x['frameVersion']
		except:
			frameVersion="Null"
		try:
			hasFoil =x['hasFoil']
		except:
			hasFoil="Null"
		try:
			hasNonFoil =x['hasNonFoil']
		except:
			hasNonFoil="Null"
		try:
			cardKingdomFoilId =x['identifiers']['cardKingdomFoilId']
		except:
			cardKingdomFoilId="Null"
		try:
			mcmId =x['identifiers']['mcmId']
		except:
			mcmId="Null"
		try:
			mcmMetaId=x['identifiers']['mcmMetaId']
		except:
			mcmMetaId="Null"
		try:
			mtgjsonV4Id =x['identifiers']['mtgjsonV4Id']
		except:
			mtgjsonV4Id="Null"
		try:
			mtgoFoilId=x['identifiers']['mtgoFoilId']
		except:
			mtgoFoilId="Null"
		try:
			mtgoId=x['identifiers']['mtgoId']
		except:
			mtgoId="Null"
		try:
			multiverseId=x['identifiers']['multiverseId']
		except:
			multiverseId="Null"
		try:
			scryfallId =x['identifiers']['scryfallId']
		except:
			scryfallId="Null"
		try:
			scryfallIllustrationId =x['identifiers']['scryfallIllustrationId']
		except:
			scryfallIllustrationId="Null"
		try:
			scryfallOracleId =x['identifiers']['scryfallOracleId']
		except:
			scryfallOracleId="Null"
		try:
			tcgplayerProductId =x['identifiers']['tcgplayerProductId']
		except:
			tcgplayerProductId="Null"
		try:
			isAlternative=x['isAlternative']
		except:
			isAlternative="Null"
		try:
			isPromo=x['isPromo']
		except:
			isPromo="Null"
		try:
			isReprint =x['isReprint']
		except:
			isReprint="Null"
		try:
			isStarter =x['isStarter']
		except:
			isStarter="Null"
		try:
			keywords =x['keywords']
		except:
			keywords="Null"
		try:
			layout =x['layout']
		except:
			layout="Null"
		try:
			legalities_commander =x['legalities']['commander']
		except:
			legalities_commander="Null"
		try:
			legalities_duel =x['legalities']['duel']
		except:
			legalities_duel="Null"
		try:
			legalities_gladiator=x['legalities']['gladiator']
		except:
			legalities_gladiator="Null"
		try:
			legalities_historic=x['legalities']['historic']
		except:
			legalities_historic="Null"
		try:
			legalities_historicbrawl=x['legalities']['historicbrawl']
		except:
			legalities_historicbrawl="Null"
		try:
			legalities_legacy =x['legalities']['legacy']
		except:
			legalities_legacy="Null"
		try:
			legalities_modern =x['legalities']['modern']
		except:
			legalities_modern="Null"
		try:
			legalities_pauper=x['legalities']['pauper']
		except:
			legalities_pauper="Null"
		try:
			legalities_paupercommander=x['legalities']['paupercommander']
		except:
			legalities_paupercommander="Null"
		try:
			legalities_penny =x['legalities']['penny']
		except:
			legalities_penny="Null"
		try:
			legalities_pioneer =x['legalities']['pioneer']
		except:
			legalities_pioneer="Null"
		try:
			legalities_premodern =x['legalities']['premodern']
		except:
			legalities_premodern="Null"
		try:
			legalities_vintage =x['legalities']['vintage']
		except:
			legalities_vintage="Null"
		try:
			manaCost =x['manaCost']
		except:
			manaCost="Null"
		try:
			manaValue =x['manaValue']
		except:
			manaValue="Null"
		try:
			name =x['name']
		except:
			name="Null"
		try:
			numbers=x['number']
		except:
			numbers="Null"
		try:
			originalText=x['originalText']
		except:
			originalText="Null"
		try:
			originalType=x['originalText']
		except:
			originalType="Null"
		try:
			power =x['power']
		except:
			power="Null"
		try:
			printings =x['printings']
		except:
			printings="Null"
		try:
			promoTypes =x['promoTypes']
		except:
			promoTypes="Null"
		try:
			cardKingdom=x['purchaseUrls']['cardKingdom']
		except:
			cardKingdom="Null"
		try:
			cardKingdomFoil=x['purchaseUrls']['cardKingdomFoil']
		except:
			cardKingdomFoil="Null"
		try:
			cardmarket=x['purchaseUrls']['cardmarket']
		except:
			cardmarket="Null"
		try:
			tcgplayer =x['purchaseUrls']['tcgplayer']
		except:
			tcgplayer="Null"
		try:
			rarity =x['rarity']
		except:
			rarity="Null"
		# print(x['rulings'])
		for k in x['rulings']:
			try:
				dates=k['date']
			except:
				dates="Null"
			try:
				textt=k['text']
			except:
				textt="Null"
		try:
			setCode=x['setCode']
		except:
			setCode="Null"
		try:
			subtypes=x['subtypes']
		except:
			subtypes="Null"
		try:
			supertypes=x['supertypes']
		except:
			supertypes="Null"
		try:
			textss=x['text']
		except:
			textss="Null"
		try:
			toughness=x['toughness']
		except:
			toughness="Null"
		try:
			typess=x['type']
		except:
			typess="Null"
		try:
			types=x['types']
		except:
			types="Null"
		try:
			uuid=x['uuid']
		except:
			uuid="Null"
		try:
		  variations=x['variations']
		except:
			variations="Null"

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
	print("----------",count)
	if count==10:
		break