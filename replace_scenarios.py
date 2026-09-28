#!/usr/bin/env python3
"""Replace only the const SCENARIOS = [ ... ]; block in index.html."""

from pathlib import Path

path = Path("/workspace/spanish-practice/index.html")
text = path.read_text(encoding="utf-8")

start_marker = "    const SCENARIOS = ["
end_marker = "    ];\n\n    /* ========== STATE ========== */"

start = text.find(start_marker)
if start < 0:
    raise SystemExit("SCENARIOS start not found")
end = text.find(end_marker, start)
if end < 0:
    raise SystemExit("SCENARIOS end not found")
# include the closing ]; 
end_close = end + len("    ];")

new_array = r'''    const SCENARIOS = [
      {
        id: "bakery",
        emoji: "🥐",
        title: "At the bakery",
        description: "Order bread, ask about pastries, and pay.",
        phrases: ["Quiero un pan", "¿Cuánto cuesta?", "Para llevar, por favor"],
        turns: [
          {
            partner: { es: "¡Buenos días! ¿Qué desea?", en: "Good morning! What would you like?" },
            choices: [
              { es: "Quiero un pan, por favor.", en: "I want a loaf of bread, please." },
              { es: "¿Tienen croissants?", en: "Do you have croissants?" },
              { es: "Busco algo dulce.", en: "I am looking for something sweet." }
            ]
          },
          {
            partner: { es: "Claro. ¿Algo más?", en: "Of course. Anything else?" },
            choices: [
              { es: "Sí. Dos croissants, por favor.", en: "Yes. Two croissants, please." },
              { es: "También quiero una barra.", en: "I also want a baguette." },
              { es: "No, solo eso. Gracias.", en: "No, just that. Thanks." }
            ]
          },
          {
            partner: { es: "¿Para llevar o para comer aquí?", en: "To go or to eat here?" },
            choices: [
              { es: "Para llevar, por favor.", en: "To go, please." },
              { es: "Para comer aquí.", en: "To eat here." },
              { es: "Para llevar. ¿Cuánto es?", en: "To go. How much is it?" }
            ]
          },
          {
            partner: { es: "Son cuatro euros cincuenta. ¿Pago con tarjeta?", en: "That is four euros fifty. Paying by card?" },
            choices: [
              { es: "Sí, con tarjeta.", en: "Yes, with a card." },
              { es: "No. Pago en efectivo.", en: "No. I am paying in cash." },
              { es: "Perfecto. Aquí tiene.", en: "Perfect. Here you go." }
            ]
          },
          {
            partner: { es: "Listo. Aquí tiene su pan. ¡Buen provecho!", en: "Done. Here is your bread. Enjoy!" },
            choices: [
              { es: "Muchas gracias. Adiós.", en: "Thank you very much. Goodbye." },
              { es: "Gracias. ¡Hasta luego!", en: "Thanks. See you later!" },
              { es: "¡Igualmente! Gracias.", en: "Likewise! Thanks." }
            ]
          },
          {
            partner: { es: "¡Que tenga un buen día!", en: "Have a nice day!" },
            choices: null
          }
        ]
      },
      {
        id: "pharmacy",
        emoji: "💊",
        title: "At the pharmacy",
        description: "Describe a symptom, ask for medicine, and check the dose.",
        phrases: ["Me duele la cabeza", "¿Tiene algo para…?", "¿Cómo lo tomo?"],
        turns: [
          {
            partner: { es: "Buenas tardes. ¿En qué puedo ayudarle?", en: "Good afternoon. How can I help you?" },
            choices: [
              { es: "Me duele la cabeza.", en: "My head hurts." },
              { es: "Necesito algo para el resfriado.", en: "I need something for a cold." },
              { es: "Busco aspirina, por favor.", en: "I am looking for aspirin, please." }
            ]
          },
          {
            partner: { es: "¿Desde cuándo se siente mal?", en: "How long have you been feeling bad?" },
            choices: [
              { es: "Desde ayer.", en: "Since yesterday." },
              { es: "Desde esta mañana.", en: "Since this morning." },
              { es: "Hace dos días.", en: "For two days." }
            ]
          },
          {
            partner: { es: "Puedo darle este jarabe. ¿Es alérgico a algo?", en: "I can give you this syrup. Are you allergic to anything?" },
            choices: [
              { es: "No. No soy alérgico.", en: "No. I am not allergic." },
              { es: "Sí. Soy alérgico a la penicilina.", en: "Yes. I am allergic to penicillin." },
              { es: "No lo sé. ¿Es seguro?", en: "I do not know. Is it safe?" }
            ]
          },
          {
            partner: { es: "Tome una cucharada cada ocho horas. ¿Tiene preguntas?", en: "Take one spoonful every eight hours. Do you have questions?" },
            choices: [
              { es: "¿Puedo tomarlo con comida?", en: "Can I take it with food?" },
              { es: "¿Cuántos días lo tomo?", en: "How many days do I take it?" },
              { es: "Entiendo. ¿Cuánto cuesta?", en: "I understand. How much does it cost?" }
            ]
          },
          {
            partner: { es: "Sí, con comida. Tres días. Son seis euros.", en: "Yes, with food. Three days. It is six euros." },
            choices: [
              { es: "Perfecto. Pago con tarjeta.", en: "Perfect. I pay with a card." },
              { es: "Gracias. Aquí tiene el dinero.", en: "Thanks. Here is the money." },
              { es: "Muy bien. Muchas gracias.", en: "Very good. Thank you very much." }
            ]
          },
          {
            partner: { es: "Que se mejore pronto.", en: "Get well soon." },
            choices: null
          }
        ]
      },
      {
        id: "train",
        emoji: "🚂",
        title: "Buying a train ticket",
        description: "Ask for a ticket, choose a time, and find the platform.",
        phrases: ["Un billete a…", "¿A qué hora sale?", "¿En qué andén?"],
        turns: [
          {
            partner: { es: "Buenos días. ¿A dónde va?", en: "Good morning. Where are you going?" },
            choices: [
              { es: "Quiero un billete a Sevilla.", en: "I want a ticket to Seville." },
              { es: "Voy a Barcelona, por favor.", en: "I am going to Barcelona, please." },
              { es: "Necesito un tren a Valencia.", en: "I need a train to Valencia." }
            ]
          },
          {
            partner: { es: "¿Ida o ida y vuelta?", en: "One way or round trip?" },
            choices: [
              { es: "Solo ida, por favor.", en: "One way only, please." },
              { es: "Ida y vuelta.", en: "Round trip." },
              { es: "Ida. ¿Cuánto cuesta?", en: "One way. How much does it cost?" }
            ]
          },
          {
            partner: { es: "Hay un tren a las diez y otro a las doce. ¿Cuál prefiere?", en: "There is a train at ten and another at twelve. Which do you prefer?" },
            choices: [
              { es: "El de las diez, por favor.", en: "The one at ten, please." },
              { es: "Prefiero el de las doce.", en: "I prefer the one at twelve." },
              { es: "¿Cuál llega antes?", en: "Which one arrives earlier?" }
            ]
          },
          {
            partner: { es: "El de las diez. Son veinticinco euros. ¿Asiento de ventana?", en: "The ten o'clock. It is twenty-five euros. Window seat?" },
            choices: [
              { es: "Sí, ventana, por favor.", en: "Yes, window, please." },
              { es: "No. Prefiero pasillo.", en: "No. I prefer aisle." },
              { es: "Me da igual. Gracias.", en: "I do not mind. Thanks." }
            ]
          },
          {
            partner: { es: "Aquí tiene su billete. Andén tres. ¡Buen viaje!", en: "Here is your ticket. Platform three. Have a good trip!" },
            choices: [
              { es: "¿Dónde está el andén tres?", en: "Where is platform three?" },
              { es: "Muchas gracias. Adiós.", en: "Thank you very much. Goodbye." },
              { es: "Perfecto. ¡Hasta luego!", en: "Perfect. See you later!" }
            ]
          },
          {
            partner: { es: "Al fondo, a la izquierda. ¡Que vaya bien!", en: "At the end, on the left. Take care!" },
            choices: null
          }
        ]
      },
      {
        id: "market",
        emoji: "🛒",
        title: "At the supermarket",
        description: "Find items, ask for help, and check out.",
        phrases: ["¿Dónde está…?", "Necesito…", "¿Está fresco?"],
        turns: [
          {
            partner: { es: "Hola. ¿Busca algo?", en: "Hi. Are you looking for something?" },
            choices: [
              { es: "Sí. ¿Dónde está la leche?", en: "Yes. Where is the milk?" },
              { es: "Busco fruta, por favor.", en: "I am looking for fruit, please." },
              { es: "¿Dónde están los huevos?", en: "Where are the eggs?" }
            ]
          },
          {
            partner: { es: "Pasillo dos, a la derecha. ¿Necesita una bolsa?", en: "Aisle two, on the right. Do you need a bag?" },
            choices: [
              { es: "Sí, una bolsa grande.", en: "Yes, a big bag." },
              { es: "No, gracias. Traigo la mía.", en: "No, thanks. I brought mine." },
              { es: "Más tarde, al pagar.", en: "Later, when I pay." }
            ]
          },
          {
            partner: { es: "Muy bien. ¿Encuentra todo bien?", en: "Very good. Are you finding everything okay?" },
            choices: [
              { es: "Sí. ¿Está fresco este pan?", en: "Yes. Is this bread fresh?" },
              { es: "Casi. ¿Dónde está el queso?", en: "Almost. Where is the cheese?" },
              { es: "Sí. ¿Cuánto cuestan las manzanas?", en: "Yes. How much do the apples cost?" }
            ]
          },
          {
            partner: { es: "Sí, es de hoy. Dos euros el kilo. ¿Algo más?", en: "Yes, it is from today. Two euros a kilo. Anything else?" },
            choices: [
              { es: "También quiero agua.", en: "I also want water." },
              { es: "No. Ya está. Gracias.", en: "No. That is all. Thanks." },
              { es: "Sí. ¿Dónde está la caja?", en: "Yes. Where is the checkout?" }
            ]
          },
          {
            partner: { es: "La caja está al frente. Son nueve euros.", en: "Checkout is at the front. That is nine euros." },
            choices: [
              { es: "Pago con tarjeta.", en: "I pay with a card." },
              { es: "Aquí tiene. Gracias.", en: "Here you go. Thanks." },
              { es: "Perfecto. ¡Hasta luego!", en: "Perfect. See you later!" }
            ]
          },
          {
            partner: { es: "¡Que tenga un buen día!", en: "Have a nice day!" },
            choices: null
          }
        ]
      },
      {
        id: "gym",
        emoji: "🏋️",
        title: "At the gym",
        description: "Sign up, ask about classes, and find the equipment.",
        phrases: ["Quiero apuntarme", "¿Hay clase de…?", "¿Dónde están las mancuernas?"],
        turns: [
          {
            partner: { es: "¡Hola! ¿Primera vez aquí?", en: "Hi! First time here?" },
            choices: [
              { es: "Sí. Quiero apuntarme.", en: "Yes. I want to sign up." },
              { es: "Sí. ¿Puedo hacer una clase de prueba?", en: "Yes. Can I do a trial class?" },
              { es: "Hola. Busco información, por favor.", en: "Hi. I am looking for information, please." }
            ]
          },
          {
            partner: { es: "Claro. Tenemos yoga, spinning y musculación. ¿Qué te interesa?", en: "Sure. We have yoga, spinning, and weights. What interests you?" },
            choices: [
              { es: "Me interesa el yoga.", en: "I am interested in yoga." },
              { es: "Prefiero musculación.", en: "I prefer weights." },
              { es: "¿A qué hora es el spinning?", en: "What time is spinning?" }
            ]
          },
          {
            partner: { es: "Hay clase a las siete. ¿Quieres ver la sala?", en: "There is a class at seven. Do you want to see the room?" },
            choices: [
              { es: "Sí, por favor.", en: "Yes, please." },
              { es: "Luego. Primero quiero apuntarme.", en: "Later. First I want to sign up." },
              { es: "¿Dónde están las mancuernas?", en: "Where are the dumbbells?" }
            ]
          },
          {
            partner: { es: "La sala está al fondo. La cuota es treinta euros al mes.", en: "The room is at the back. The fee is thirty euros a month." },
            choices: [
              { es: "Perfecto. Me apunto.", en: "Perfect. I will sign up." },
              { es: "¿Incluye las clases?", en: "Does it include the classes?" },
              { es: "Bien. ¿Necesito toalla?", en: "Good. Do I need a towel?" }
            ]
          },
          {
            partner: { es: "Sí, incluye todo. Trae toalla y agua. ¿Empezamos hoy?", en: "Yes, it includes everything. Bring a towel and water. Shall we start today?" },
            choices: [
              { es: "Sí. Empezamos hoy.", en: "Yes. We start today." },
              { es: "Mañana, por favor.", en: "Tomorrow, please." },
              { es: "Genial. Muchas gracias.", en: "Great. Thank you very much." }
            ]
          },
          {
            partner: { es: "¡Bienvenido al gimnasio!", en: "Welcome to the gym!" },
            choices: null
          }
        ]
      },
      {
        id: "bank",
        emoji: "🏦",
        title: "At the bank",
        description: "Open an account, ask about cards, and make a deposit.",
        phrases: ["Quiero abrir una cuenta", "Necesito una tarjeta", "Quiero ingresar dinero"],
        turns: [
          {
            partner: { es: "Buenos días. ¿En qué puedo ayudarle?", en: "Good morning. How can I help you?" },
            choices: [
              { es: "Quiero abrir una cuenta.", en: "I want to open an account." },
              { es: "Necesito una tarjeta, por favor.", en: "I need a card, please." },
              { es: "Quiero ingresar dinero.", en: "I want to deposit money." }
            ]
          },
          {
            partner: { es: "Por supuesto. ¿Tiene su documento de identidad?", en: "Of course. Do you have your ID?" },
            choices: [
              { es: "Sí. Aquí tiene mi pasaporte.", en: "Yes. Here is my passport." },
              { es: "Sí. Tengo el DNI.", en: "Yes. I have my ID card." },
              { es: "Un momento. Lo busco.", en: "One moment. I will look for it." }
            ]
          },
          {
            partner: { es: "Gracias. ¿Cuenta corriente o de ahorro?", en: "Thanks. Checking or savings account?" },
            choices: [
              { es: "Cuenta corriente, por favor.", en: "Checking account, please." },
              { es: "De ahorro.", en: "Savings." },
              { es: "¿Cuál me recomienda?", en: "Which one do you recommend?" }
            ]
          },
          {
            partner: { es: "La corriente es más práctica. ¿Quiere también una tarjeta?", en: "Checking is more practical. Do you also want a card?" },
            choices: [
              { es: "Sí, quiero una tarjeta.", en: "Yes, I want a card." },
              { es: "Sí. ¿Cuánto cuesta al mes?", en: "Yes. How much does it cost per month?" },
              { es: "Por ahora, solo la cuenta.", en: "For now, just the account." }
            ]
          },
          {
            partner: { es: "La tarjeta cuesta dos euros al mes. ¿Ingresa dinero hoy?", en: "The card costs two euros a month. Are you depositing money today?" },
            choices: [
              { es: "Sí. Cien euros, por favor.", en: "Yes. One hundred euros, please." },
              { es: "No. Otro día.", en: "No. Another day." },
              { es: "Sí. ¿Puedo hacerlo aquí?", en: "Yes. Can I do it here?" }
            ]
          },
          {
            partner: { es: "Listo. Su cuenta está abierta. ¡Bienvenido!", en: "Done. Your account is open. Welcome!" },
            choices: null
          }
        ]
      }
    ];'''

new_text = text[:start] + new_array + text[end_close:]
path.write_text(new_text, encoding="utf-8")
print("Replaced SCENARIOS OK")
print(f"Old span bytes: {end_close - start}")
print(f"New array bytes: {len(new_array)}")
print(f"File size now: {path.stat().st_size}")
