# Life-Expectancy-Predictor 🌍

A modern, interactive web application built with Streamlit that predicts life expectancy based on various health, economic, and social factors. The application uses machine learning to provide accurate predictions and presents them through an intuitive, data-rich interface with interactive visualizations.



## 🌟 Features

- Interactive prediction interface with real-time updates
- Rich data visualization using Plotly
- Comprehensive health and economic factors analysis
- Global comparison metrics
- Intuitive tab-based navigation
- Responsive design
- Accessibility-focused UI

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/life-expectancy-predictor.git
cd life-expectancy-predictor
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Download the trained model:
```bash
mkdir models
# Download the model file and place it in the models directory
# You can either use the provided script:
python download_model.py
# Or manually download from the releases page and place in models/life_expectancy_model.pkl
```

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

## 📦 Project Structure

```
life-expectancy-predictor/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Project dependencies
├── download_model.py       # Script to download the trained model
│
├── models/
│   └── life_expectancy_model.pkl  # Trained prediction model
│
├── demo/                   # Demo images and videos
│   └── demo.gif
│
└── README.md              # Project documentation
```

## 📋 Requirements

- streamlit>=1.10.0
- pandas>=1.3.0
- plotly>=5.3.0
- scikit-learn>=0.24.2
- numpy>=1.19.5

## 🔧 Configuration

The application can be configured through `config.yaml` or environment variables:

```yaml
model_path: "models/life_expectancy_model.pkl"
default_country: "Global"
theme: "light"
```

## 🎯 Usage Example

1. Navigate to the "Health Factors" tab
2. Adjust sliders for health indicators
3. Move to "Economic Factors" and set relevant values
4. Select country and development status
5. View the prediction and analysis in the right panel

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- WHO for providing health statistics data
- World Bank for economic indicators
- Streamlit team for the amazing framework
- Contributors and maintainers of all dependencies

## 📧 Contact

Your Name - [@Sarankumar](https://twitter.com/yourusername)

Project Link: [https://github.com/sarankumar1325/life-expectancy-predictor](https://github.com/yourusername/life-expectancy-predictor)

## ⭐ Support

If you find this project useful, please consider giving it a star on GitHub!

---
Made with ❤️ for better health predictions
