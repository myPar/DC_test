# Задание 1

#### Решение

Данное задание требует реализовать вычленение текста по шаблону и по максимальному правдоподобию. Я решил написать python программу, которая использует готовые датасеты с городами СНГ и ищет в тексте сообщения токен максимально похожий на один из городов. 

Суммарный объём всех датасетов составляет около 60кб, что ничтожно мало по сравнению с весом любой LLM. Более того, LLM будет работать на порядок медленнее, поскольку даже один токенайзер использует словарь объёма несколько мегабайт, соответственно разбиение токенайзером уже займёт гораздо больше времени, чем сравнение всех слов сообщения со всеми городами в датасетах.

В виду этого, посчитал использование LLM в рамках данного задания нецелесообразным.

# Задание 2

### Решение

От сервиса нам хотелось бы получать генерацию относительно креативных поздравлений, к тому же с различным выходом от вызова к вызову. Здесь как раз подойдёт генеративная LLM-модель. Более того, мне очень хотелось попробовать с такими поработать.

Я выбрал открытую, основанную на архитектуре GPT-2 модель от сбера - **ruGPT3Large** (Меня тоже смутило GPT3 в названии модели, на самом деле она основана на GPT2). В библиотеке transformers с huggingface она соответствует классу **GPT2LMHeadModel**. Больше информации об открытых моделях сбера, можно посмотреть на их [официальном GitHub](https://github.com/ai-forever/ru-gpts)



# Как запустить у себя