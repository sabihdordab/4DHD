# 🎮 Character Creator Game

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-00599C?style=for-the-badge&logo=python&logoColor=white)

![demo](/assets/demo.png)
</div>

---

## Features

- **Body Types**
- **Skin Tones**
- **Clothing**
- **Hairstyles**
- **Guns**
- **Wings**
- **Eye Styles**
- **Color Palette**
- ...
  
---

### Prerequisites
```bash
pip install pygame
```

### Installation
1. Clone the repository
```bash
git clone https://github.com/sabihdordab/4DHD.git
cd 4DHD
```

2. Run the game

```bash
python main.py
```

## 🏗️ Project Structure

```
4DHD/
├── main.py                 
├── model/
│   ├── character.py        
│   └── style/
│       ├── female/         
│       │   ├── shirt.txt
│       │   ├── hair.txt
│       │   ├── eye.txt
|       |   ├── eye.txt
|       |   ├── etc...
│       │   └── pants.txt
│       └── male/           
│           ├── shirt.txt
│           ├── hair.txt
│           ├── eye.txt
│           └── pants.txt
|           ...
└── README.md
```

---


## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Add New Styles**: Create new character elements in the style files
2. **Expand Color Palettes**: Add more color options
3. **Improve UI**: Enhance the user interface
4. **Add Features**: Implement new customization options

### Adding New Styles
1. Create polygon coordinates for your design
2. Add to appropriate `.txt` file in `model/style/[character]/`
3. Follow the existing format: `[[(x1,y1), (x2,y2), ...], color]`

---


## 🎯 Future Features

- [ ] **More Body Types**: Additional character templates
- [ ] **Accessories**: Hats, glasses, jewelry
- [ ] **Background Selection**: Custom backgrounds for characters
- [ ] **Animation Preview**: See characters in motion
- [ ] **Export Options**: Save as image files