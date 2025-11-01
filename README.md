

# 🕹️ HollowKnight- A 2D Platformer  
**Mini Project Report and Documentation**

## 🎮 Project Overview  
This project is a 2D side-scrolling platformer game inspired by the atmospheric style and mechanics of Hollow Knight. Developed using Python and the Pygame library, the game features custom-designed characters, immersive backgrounds, dynamic music scores, and a seamless menu-to-gameplay experience.

The project was undertaken as part of our academic mini project to explore the fundamentals of game development, collaborative software engineering, and version control using GitHub.

---

## 🎯 Objectives  
- Design and develop a functional 2D platformer game in Python  
- Implement smooth character movement, level transitions, and enemy interactions  
- Integrate custom visual and audio assets for immersive gameplay  
- Develop GUI screens for menus and game flow  
- Collaborate effectively using Git and GitHub  
- Document the development process and technical decisions

---

## 🛠️ Technologies Used  

| Category            | Tools Used             |
|---------------------|------------------------|
| Programming Language| Python                 |
| Game Framework      | Pygame-CE                |
| IDE                 | Visual Studio Code     |
| Graphics Design     | Photoshop, Tiled       |
| Audio Composition   | FL Studio, Audacity    |
| Version Control     | Git and GitHub         |

---

## ✨ Features Implemented  
- Custom character sprites and animations  
- Atmospheric background art and parallax scrolling  
- Original background music and sound effects  
- Menu system with start, pause, and resume functionality  
- Game loop with level progression and enemy encounters  
- Synchronization between menu and in-game states  
- Collision detection and player physics  
- Modular code structure for scalability

---

## 🔄 Project Flow  
1. **Main Menu**  
   - Start Game, Continue , Settings, Exit options  
   - Smooth transition into gameplay  

2. **Gameplay**  
   - Navigate through handcrafted levels  
   - Encounter enemies, avoid traps, and collect items  
   - Background music adapts to level progression  

3. **Game Over / Victory Screen**  
   - Displays final score and restart option  

---

## 👥 Team Members and Contributions  

| Name           | Contribution Summary                                                                 |
|----------------|----------------------------------------------------------------------------------------|
| **Mission Adak** | Designed and implemented all character sprites and animations. Created immersive background art and composed original background music scores. Structured the visual and audio experience of the game. |
| **Devansh**      | Developed the menu system, main game loop, and ensured synchronization between menu transitions and gameplay continuation. Focused on game state management and user interface logic. |
| **Both**         | Collaboratively conceptualized the game idea, including character roles, level themes, enemy types, and overall gameplay mechanics. Jointly researched platformer design principles and Hollow Knight inspirations. |

---

## 📁 File-Wise Commit Responsibilities  

| File / Folder             | Description                                      | Committed By     |
|---------------------------|--------------------------------------------------|------------------|
| `main.py`                 | Game loop, input handling, and transitions       | Mission and Devansh          |
| `menu.py`                 | Menu logic and GUI flow                          | Devansh Gujarathi         |
| `player.py`               | Character movement and animation                 | Mission Adak     |
| `sprites.py`              | Sprite definitions and asset loading             | Mission Adak     |
| `support.py`              | Utility functions and helpers                    | Devansh Gujarathi     |
| `/assets/backgrounds`     | Background art and visual themes                 | Mission Adak     |
| `/assets/music`           | Background music and sound effects               | Mission Adak     |
| `/levels`                 | Level design and layout                          | Both             |
| `README.md`               | Project documentation and report                 | Both             |

Final GitHub commited by Mission Adak
---

## 🔧 GitHub Workflow  
- Separate branches were maintained for each module  
- Pull requests were used for weekly merges and reviews  
- Clear commit messages documented progress  
- Merge conflicts were resolved through team coordination  

---

## ⚠️ Challenges Faced  
- **Menu Synchronization**: Ensuring smooth transitions between menu and gameplay required careful state management.  
- **Audio Timing**: Background music had to be timed with level progression and player actions.  
- **Sprite Alignment**: Initial character sprites didn’t align well with platform tiles, requiring rework.  
- **Frame Rate Drops**: Optimized sprite redraws and asset loading to maintain performance.
- **Character Change**: We tried fix the character with Knight but it didn't go well in synchronization with background tiles and while in movement duplicate characters were appearing. Which Leads to Huge Delay in the Project 

---

## 🚧 What Didn’t Go as Planned  
- Boss-level mechanics were scoped out due to animation complexity  
- Settings and customization menu postponed for future update  
- Multi-character , doing this was tough because of animations and proper sync needs to be there . ( already have the knight character folder inside the graphics folder)  

---

## 🔮 Future Improvements  
- Add boss fights and advanced enemy AI  
- Introduce checkpoints and save/load system  
- Expand level variety with new environments  
- Implement local co-op or multiplayer mode  
- Optimize rendering and memory usage  
- Add controller support and customizable key bindings
- Adding New Characters and Weapons

---

## 📚 Documentation Summary  

| File         | Purpose                                         |
|--------------|-------------------------------------------------|
| `main.py`    | Game loop, state transitions, and event handling|
| `player.py`  | Player physics, input, and animation            |
| `menu.py`    | Menu logic and GUI transitions                  |
| `sprites.py` | Sprite definitions and asset management         |
| `/levels`    | Platform layouts and level progression          |
| `/assets`    | All images, sounds, and music files             |

---

## 🎓 Learning Outcomes  
- Gained hands-on experience in 2D game development using Python  
- Learned sprite animation, physics simulation, and GUI integration  
- Practiced modular programming and team-based collaboration  
- Applied Git workflow for version control and project management  
- Understood challenges in real-time rendering and game optimization
- Learned not only pygame library but also pygame-ce , math library inside pygame , tmx and tiles etc

---

## 📌 Submission Details  
- **Project Title**: HollowKnight- A 2D Platformer  
- **Course**: Mini Project – Game Development using Python  
- **Team Size**: 2 Members  
- **Duration**: 3 weeks ( 2 weeks for research and 9 days to code) 
- **Team Members**:  
  - Mission Adak  
  - Devansh Gujarathi

---

## Controls

- Arrow keys: Move the character
- Space: Jump
- Z: Attack
- ESC: Pause/Menu

## Development

Developed by MissionAdak and DevanshGujarathi 


