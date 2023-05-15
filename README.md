### Клон инстаграмма FastApi - бэкэнд, React - фронтэнд.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Izpodvypodvert/FastAPI-React-Insta-Clone.git
```

```
cd FastAPI-Insta-Clone
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Запустить бэкэнд:

```
uvicorn main:app --reload
```

Перейтив папку с фронтэндом:

```
cd fastapi-insta-clone-frontend
```

Установить зависимости:

```
npm i
```

Запустить:

```
npm run start
```
