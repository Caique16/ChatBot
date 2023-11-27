# pip install nltk
import nltk
from nltk.chat.util import Chat, reflections

def chatbot():
    print("¡Hola! Soy un asistente virtual de la tienda. ¿En qué puedo ayudarte hoy?")

    # Definición de los pares de patrones y respuestas
    pairs = [
        [r"mi nombres es(.*)", ["¡Hola %1! ¿En qué puedo ayudarte hoy?"]],
        [r"cual es tu nombre?", ["Soy el asistente virtual de la tienda. ¿En qué puedo ayudarte?"]],
        [r"cómo estas?", ["Estoy aquí para ayudarte. ¿En qué puedo hacerlo?"]],
        [r"adios", ["Hasta luego. ¡Que tengas un buen día!"]],
        [r"cuál es tu color favorito?", ["No tengo un color favorito, pero estoy aquí para responder tus preguntas sobre la tienda."]],
        [r"qué puedes hacer?", ["Puedo ayudarte a encontrar productos, responder preguntas sobre la tienda y procesar pedidos. ¿En qué necesitas ayuda?"]],
        [r"productos", ["Tenemos una amplia variedad de productos. ¿Buscas algo en particular?"]],
        [r"información de (.*)", ["¿Qué información específica estás buscando sobre %1?"]],
        [r"cómo puedo realizar un pedido", ["Puedes agregar productos a tu carrito y luego proceder al pago. ¿Necesitas ayuda con algo en específico?"]],
        [r"carrito de compras", ["Puedo ayudarte a ver o modificar los artículos en tu carrito de compras. ¿Quieres hacer algo en particular?"]],
        [r"ayuda", ["Estoy aquí para ayudarte. ¿En qué puedo hacerlo?"]],
        [r".*", ["Lo siento, no entiendo. ¿Puedes reformular tu pregunta?"]],
    ]

    reflections = {
        "yo": "tú",
        "tú": "yo",
        "mi": "tu",
        "tu": "mi",
    }

    # Creación del chatbot
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    nltk.download("punkt")
    chatbot()