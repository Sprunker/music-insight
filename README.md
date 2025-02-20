# Music Genre Detection / Detección de Géneros Musicales

This project is an API that allows automatic detection of music genres from audio files. It uses advanced signal processing and machine learning techniques to analyze the characteristics of audio tracks and classify them into different genres. The API is built with **FastAPI**, enabling efficient performance and easy scalability.

Additionally, **AcoustID** is used to obtain metadata from audio tracks, enriching the information about the songs, such as title, artist, and album, thereby improving the accuracy of genre classification.

Este proyecto es una API que permite la detección automática de géneros musicales a partir de archivos de audio. Utiliza técnicas avanzadas de procesamiento de señales y aprendizaje automático para analizar las características de las pistas de audio y clasificarlas en diferentes géneros. La API está construida con **FastAPI**, lo que permite un rendimiento eficiente y una fácil escalabilidad.

Además, se utiliza **AcoustID** para la obtención de metadata de las pistas de audio, lo que permite enriquecer la información sobre las canciones, como el título, el artista y el álbum, mejorando así la precisión en la clasificación de géneros.

## Main Features / Características Principales

- **Audio File Upload**: Users can send audio files in formats like MP3 and WAV for analysis through the API.
- **Genre Detection**: Utilizes pre-trained models to identify the musical genre of the uploaded audio track.
- **Metadata Retrieval**: Uses **AcoustID** to obtain metadata from audio tracks, enriching the information about the songs.
- **RESTful API**: The application exposes a RESTful API that allows integration with other applications and services.
- **Support for Multiple Genres**: Ability to classify a wide variety of musical genres, from pop and rock to jazz and classical.

- **Carga de Archivos de Audio**: Los usuarios pueden enviar archivos de audio en formatos como MP3 y WAV para su análisis a través de la API.
- **Detección de Géneros**: Utiliza modelos preentrenados para identificar el género musical de la pista de audio cargada.
- **Obtención de Metadata**: Se utiliza **AcoustID** para la obtención de metadata de las pistas de audio, lo que permite enriquecer la información sobre las canciones.
- **API RESTful**: La aplicación expone una API RESTful que permite la integración con otras aplicaciones y servicios.
- **Soporte para Múltiples Géneros**: Capacidad para clasificar una amplia variedad de géneros musicales, desde pop y rock hasta jazz y clásica.

## Installation and Usage / Instalación y Uso

### English Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Sprunker/music-insight.git
   cd music-insight
   ```

2. **Build the Docker Image**:
   ```bash
   docker build -t music-insight .
   ```

3. **Run the API**:
   ```bash
   docker run -p 8000:8000 music-insight
   ```

4. **Access the API Documentation**: Open your browser and go to `http://localhost:8000/docs#/` to interact with the API.

### Instrucciones en Español

1. **Clonar el Repositorio**:
   ```bash
   git clone https://github.com/Sprunker/music-insight.git
   cd music-insight
   ```

2. **Construir la Imagen de Docker**:
   ```bash
   docker build -t music-insight .
   ```

3. **Ejecutar la API**:
   ```bash
   docker run -p 8000:8000 music-insight
   ```

4. **Acceder a la Documentación de la API**: Abre tu navegador y ve a `http://localhost:8000/docs#/` para interactuar con la API.

## Contributions / Contribuciones

Contributions are welcome. If you want to improve the project, please open an issue or submit a pull request.

Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, por favor abre un issue o envía un pull request.

## License / Licencia

This project is licensed under the Affero General Public License v3 (AGPLv3), which allows for use, modification, and distribution, provided that the source code of modifications is shared and the same license is maintained.

Este proyecto está bajo la Licencia Affero General Public License v3 (AGPLv3), lo que permite su uso, modificación y distribución, siempre que se comparta el código fuente de las modificaciones y se mantenga la misma licencia.