# -*- coding: utf-8 -*- 
#!/usr/bin/python3.8
import json
import random

dicts = {
		'design': 'дизайн', 'choice': 'выбор', 'develop': 'разработка','accountant': 'бухгалтер', 
		'single': 'холост', 'married': 'женатый', 'chair': 'стул', 'cheap': 'дешевый', 'expensive': 'дорогой', 
		'grass': 'трава', 'sun': 'солнце', 'show': 'снег', 'charger': 'зарядка', 'housewife': 'домохозяйка', 'busy': 'занятой',
		'heavy': 'тяжелый', 'boarding pass': 'посадочный талон', 'a lot of': 'много',  'bag': 'сумка', 'suitcase': 'чемодан',
		'discover': 'обнаружить', 'divorced': 'разведн', 'laptor': 'ноутбук', 'brown': 'коричневый', 'diary': 'дневник', 
		'widowed': 'вдовец', 'husband': 'муж', 'lawyer': 'юрист',	
		'make up bag': 'косметичка', 'umbrella': 'зонтик', 'luggage': 'ручная кладь', 'scissors': 'ножницы',
		'glasses': 'очки', 'nephew': 'племянник', 'niece': 'племянница', 'glad': 'радостный',
		'sweet': 'симпатичная', 'flight': 'рейс', 'so': 'такой', 'again': 'снова', 'when': 'когда',
		'to': 'до', 'past': 'после', 'what': 'что', 'where': 'куда', 'who': 'кто', 'departure': 'вылет',
		'gate': 'ворота', 'remark': 'комментарий', 'delayed': 'задержан', 'boarding': 'посадка', 'desk': 'стойка', 'call': 'вызов',		
		}
dicts_two = {
		'also': 'также', 'seat': 'место', 'same': 'одинаковый', 'account': 'счет', 'railway': 'железная дорога',
		'aisle': 'проход между креслами', 'magazine': 'журнал', 'head': 'голова', 'here you are': 'вот пожалуйста',
		'here it is': 'вот он', 'warm': 'теплый', 'windy': 'ветренный', 'small': 'маленький','rude': 'грубый',
		'armchair': 'кресло', 'rug': 'ковер', 'sofa': 'диван', 'bedroom': 'спальня',
		'pillow': 'подушка', 'pillow case': 'наволочка', 'quite': 'довольно', 'enought': 'достаточно',
		'whose': 'чей','behind': 'за', 'next to': 'рядом', 'flight attendant': 'бортпроводник',  
		'boring': 'скучный', 'ugly': 'некрасивый', 'under': 'под', 'sheet': 'простыня', 'mirror': 'зеркало',
		'cup': 'чашка', 'cupboard': 'шкаф', 'duvet': 'одеяло', 'lamp': 'лампа', 'comfortable': 'удобный',
		'spoon': 'ложка', 'glass': 'стакан', 'knife': 'нож',
		'chest of drawers': 'камод', 'kitchen': 'кухня', 'bedside table': 'прикроватный столик',
		'wardrobe': 'платяной шкаф', 'hanger': 'плечики для одежды',
		'oven': 'духовка', 'cooker': 'плита', 'fridge': 'холодильник', 'microwave': 'микроволновка', 'sink': 'раковина',
		'teapot': 'заварочный чайник', 'plate': 'тарелка', 'fork': 'вилка', 'tin opener': 'консервный нож', 'corkscrew': 'штопор', 
		}
dicts_three = {
	    'toothbrush': 'зубная щетка', 'toothpaste': 'зубная паста', 'tap': 'кран', 'bath': 'ванна',
	    'shower': 'душ', 'maybe': 'может быть', 'bowl': 'миска',
	    'empty': 'пустой', 'poor': 'бедный', 'cabbage': 'капуста', 'ham': 'ветчина', 'bread': 'хлеб', 'butter': 'масло(сливочное)',
	    'carton': 'пакет картонный', 'bag': 'мешок', 'packet': 'упаковка', 'piece': 'кусочек', 'slice': 'ломтик',
	    'washbasin': 'умывальник', 'bathrobe': 'халат', 'towel': 'полотенце', 'kettle': 'чайник', 'Sunday': 'воскресенье',
	    'Monday': 'понедельник', 'Tuesday': 'вторник', 'Wednesday': 'среда', 'Thursday': 'четверг', 'Friday': 'пятница',
	    'Saturday': 'суббота', 'theatre': 'театр', 'social': 'общественный', 'event': 'мероприятие', 
	    'sightseeing': 'осмотр достопримечательностей', 'tour': 'путешествие', 'trip': 'короткая поездка', 
	    'walking': 'пешая', 'excursion': 'экскурсия', 'around': 'вокруг', 'tea garden': 'чайная на открытом воздухе',
	    'furniture': 'мебель', 'vegetables': 'овощи', 'beans': 'фасоль', 'tuna': 'тунец', 'soup': 'суп',
		 }
dicts_four ={
		'meet': 'встречаться', 'maths': 'математика', 'long': 'долгий', 'sweets': 'сладости', 'get up': 'вставать',
		'stay': 'оставаться', 'wake up': 'разбудить', 'wash': 'умываться', 'go for a walk': 'ходить на прогулку',
		'teeth': 'зубы',
		'hate': 'ненавидеть', 'cook': 'готовить', 'journey': 'путешествие', 'talk': 'разговаривать', 'usually': 'обычно',
		'often': 'часто', 'early': 'рано', 'late': 'поздно', 'till': 'пока', 'brush': 'чистить', 'get dressed': 'одеваться',
		'chicken': 'курица', 'beef': 'говядина', 'pork': 'свинина', 'lamb': 'баранина', 'soup': 'суп', 'crisps': 'чипсы',
		'cream': 'сливки', 'cake': 'торт', 'flakes': 'хлопья', 'do the washing': 'стирать', 'do the washing up': 'мыть посуду',
		'do the ironing': 'гладить', 'us': 'нас', 'him': 'ему', 'her': 'её', 'them': 'их', 'his': 'его',
}		 
dicts_five = {
		'ice skating': 'фигурное катание', "chemist's": 'аптека', 'bridge': 'мост',  "it's on your left": 'это слева от вас',
		'art gallery': 'художественная галерея', 'post office': 'почтовое отделение', 
		'cycling': 'велоспорт', 'sailing': 'парусный спорт','pond': 'пруд', 'underground station': 'станция метро', 
		"you can't miss it": 'вы это не пропустите',
		'enjoy': 'наслаждаться', 'hope': 'надеяться', 'turn': 'повернуть', 'cross': 'пересекать', 'along': 'вдоль',
		'past': 'мимо', 'over': 'по', 'through': 'сквозь', 'path': 'тропинка', 'want': 'хотеть', 'need': 'нуждаться',
		'opposite': 'напротив', 'church': 'церковь',
}

dicts_six = {
		'slim': 'стройный', 'overweight': 'полный', 'bit': 'немного', 'good-looking': 'привлекательный', 'tall': 'высокий',
		'hair': 'волосы', 'short': 'короткие', 'straight': 'прямые(волосы)', 'curly': 'кудрявые(волосы)', 'south': 'юг',
		'wavy': 'волнистые(волосы)', 'eyes': 'глаза', 'skin': 'кожа', 'dark': 'темная(кожа, волосы)', 'ancient': 'древний',
		'fair': 'светлая(кожа, волосы)', 'ruin': 'руины', 'garden': 'сад', 'sunset': 'закат', 'fight': 'драка', 'meal': 'еда',
		'hole': 'нора', 'afraid': 'испуганный', 'snake': 'змея', 'flavor': 'аромат',
		'plain': 'равнина', 'gloomy': 'мрачный',
		'frighten': 'пугать', 'lonely': 'одинокий', 'sincere': 'искренний*',
		'prepare': 'готовиться', 'gather': 'собираться', 'desperately': 'отчаянно*', 'miss': 'скучать',
}

dicts_seven = {
		'exciting': 'захватывающе', 'dirty': 'грязный', 'tidy': 'аккуратный', 'handsome': 'красивый(о мужчинах)',
		'great': 'великий', 'hot': 'горячий', 'safe': 'безопасный', 'slow': 'медленный', 'fast': 'быстрый',
		'far': 'далекий', 'noisy': 'шумный', 'quiet': 'тихий', 'wet': 'мокрый', 'dry': 'сухой', 'entry': 'вход',
		'belive': 'верить', 'exactly': 'точно', 'wear': 'носить', 'famous': 'известный', 'spring': 'весна',
		'autumn': 'осень', 'awful': 'ужасно', 'clever': 'умный', 'band': 'музыкальная группа', 'born': 'родившийся',
		'the keyboards': 'клавишные инструменты', 'the drums': 'ударные инструменты', 'lead': 'ведущий', 
		'singer': 'певец', 'songwriter': 'автор песен', 'star': 'звезда',
		'innovative': 'новаторский', 'others': 'другие', 'still': 'все ещё', 'drummer': 'барабанщик', 'rhythm': 'ритм',
		'the charts': 'хит-парад', 'around': 'вокруг', 'event': 'событие', 'amazing': 'невероятный', 'stage': 'сцена',
		'fun': 'веселье', 'defender': 'защитник', 'motherland': 'отечество', 'cosmonautics': 'космонавтика',
		'orthodox': 'православный', 'Easter': 'Пасха', 'victory': 'победа', 'faithfulness': 'верность', 
		'knowledge': 'знания', 'unity': 'единство', 'international': 'международный',
}

dicts_eight = {
		'arrive': 'прибывать', 'laugh': 'смеяться', 'tasty': 'вкусный', 'delicious': 'деликатес', 'queen': 'королева',
		'admir': 'восхищаться', 'palace': 'дворец', 'lawn': 'лужайка', 'sunbathe': 'загорать', 'tired': 'уставший',
		'on the way home': 'по дороге домой', 'decide': 'решил', 'cry': 'плакать', 'try': 'пробовать', 'fry': 'жарить',
		'drop': 'ронять', 'bark': 'лаять', 'mountain': 'гора', 'cancel': 'отменить', 'rent': 'брать в аренду',
		'hill': 'холм', 'scenery': 'пейзаж', 'castle': 'замок', 'located': 'расположенный', 'shorelain': 'береговая линия',
		'medieval': 'средневековый', 'tide': 'прилив', 'view': 'вид', 'lake': 'озеро', 'rain': 'дождь',
		'souvenir': 'сувенир', 'fortunately': 'к счастью', 'relative': 'родственник', 'back': 'назад',
		'midnight': 'полночь', 'market': 'рынок', 'spicy': 'пряный',
		}
dicts_nine = {
		'suspicious': 'настороженный', 'hude': 'огромный', 'unfortunately': 'к сожалению', 'except': 'за исключением',
		'unusual': 'необычный', 'overnight': 'на ночь', 'hit': 'ударить', 'bury': 'похоронить', 'sad': 'печальный',
		'tear': 'слеза', 'suddenly': 'вдруг', 'middle': 'середина', 'noise': 'шум', 'sill': 'подоконник',
		'beloved': 'любимый', 'alive': 'живой', 'hold': 'держать', 'shoked': 'шокированный', 'then': 'тогда',
		'on my way': 'по дороге', 'mind': 'возвращаться', 'safe and sound': 'цел и невредим',
		'at the same time': 'одновременно', 'tomb': 'могила', 'later': 'позже', 'neighbour': 'соседка',
		'sure': 'конечно', 'just': 'просто', 'invite': 'приглашать', 'hope': 'надеяться', 'review': 'обзор',
		"Let's": 'давай(приглашение к действию)',
}
dicts_ten = {
		'guess': 'догадываться', 'hope': 'надеяться', 'clothes': 'одежда', 'wrong': 'неправильный', 'worry': 'беспокоиться',
		'drink like a fish': 'пить много алкоголя', 't-shirt': 'футболка', 'trainers': 'кросовки', 'trousers': 'брюки',
		'shirt': 'рубашка', 'skirt': 'юбка', 'blouse': 'блузка', 'suit': 'костюм', 'tie': 'галстук', 'dress': 'платье',
		'jumper': 'джепер', 'jacket': 'жакет', 'sweater': 'свитер', 'coat': 'пальто', 'shoes': 'обувь',
		'boots': 'сапоги', 'cap': 'кепка', 'move': 'двигаться', 'take': 'брать', 'year-off': 'академичесий отпуск',
		'native': 'родной(язык)', 'foreign': 'иностранный', 'i would like': 'мне бы хотелось', 'thirsty': 'испытывающий жажду',
		'turn off': 'выключать', 'probably': 'возможно', 'might': 'может быть'
}
dicts_eleven = {
		'wedding': 'свадьба', 'ceremony': 'церемония', 'orchestra': 'оркестр', 'immediate relatives': 'близкие родственники',
		'close friends': 'близкие друзья', 'honeymoon': 'медовый месяц', 'live happily even after': 'жить долго и счастливо',
		'celebrate': 'отмечать', 'annivesary': 'годовщина', 'send': 'отправлять', 'which': 'который', 'ride': 'поездка верхом',
		'congratulations': 'поздравления', 'boat': 'лодка', 'camel': 'верблюд', 'sphinx': 'сфинкс', 'pyramid': 'пирамида',
		'guided tour': 'экскурсия с гидом', 'duck': 'утка', 'oyster': 'устрица', 'palace square': 'дворцовая площадь',
		'ache': 'боль', 'headache': 'головная боль', 'sore throat': 'воспаленое горло', 'toothache': 'зубная боль',
		'back': 'спина', 'leg': 'нога', 'stomack': 'желудок', 'heart': 'сердце', 'cold': 'простуда', 'cough': 'кашель',
		'ill': 'больной', 'sick': 'испытывающий тошноту', 'terrible': 'ужасный',
}

dicts_twelwe = {
		'medicine': 'лекарство', 'painkiller': 'болеутоляющее', 'day off': 'отгул', 'take some medicine': 'принимать лекарства',
		'take the day off': 'брать отгул', 'smoke': 'курить', 'fracture': 'перелом', 'faculty': 'факультет', 'part': 'часть',
		'even': 'даже', 'self-guided': 'самостоятельный', 'forget': 'забывать', 'lost': 'потерянный', 'landscape': 'ландшафт',
		'mysterious': 'таинственный', 'ancient': 'древний', 'jungle': 'джунгли', 'up to now': 'к настоящему моменту',
		'more': 'более',
}

dicts_thirteen = {
		'roasted': 'запеченый в духовке', 'grilled': 'жареный на гриле', 'fried': 'жареный', 'boiled': 'вареный', 'still': 'без газа',
		'sparking': 'газированный', 'mushroom': 'гриб', 'pound': 'фунт стерлингов', 'main courses': ' основное блюдо',
		'order': 'заказывать', 'bill': 'счет в ресторане', 'try on': 'примерять', 'fit': 'подходить (по размеру)', 'suit': 'подходить(быть к лицу)',
		'a fitting room': 'примерочная', 'cash': 'наличные', 'customer': 'покупатель', 'earn': 'зарабатывать', 'salary': 'ежемесячная зарплата',
		'tiring': 'утомительный', 'bring': 'приносить', 'shift': 'смена', 'work shift': 'работать посменно', 'certainly': 'безусловно'
}
all = {
	'quite': 'довольно', 'enought': 'достаточно', 'sink': 'раковина',
}

# try = {
# 	'enything else': 'что-нибудь еще',
# }

with open('dict.txt', 'w') as f:
	json.dump(dicts_thirteen, f)

with open('dict.txt', 'r') as f:
	myDict = json.load(f)


english = []
russia = []
for i, n in myDict.items():
	english.append(i)
	russia.append(n)

def dict_english():
	eng_random = english[random.randint(0, (len(english) - 1))]
	while 1>0:		
		a = input('Введите перевод к слову' + ' ' + myDict[eng_random] + ':')				
		if eng_random == a:
			print('ok')
			dict_english()
		elif a == '0':
			break		
		else:
		 	print('ответ не верен')
		 	continue

def dict_russian():
	rus_random = random.choice(english)
	while 1>0:
		a = input('Введите перевод к слову' + ' ' + rus_random + ':')
		if a == myDict[rus_random]:
			print('ok')
			dict_russian()
		elif a == '0':
			break
		else:
			continue
def russian():
	print(russia)



choice = input("Введите число 1 для вывода русских слов и 2 для вывода английских:")
if choice == '1':
	dict_english()
elif choice =='2':
	dict_russian()
else:
	russian()