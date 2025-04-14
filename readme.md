# 📷 Calibration de la caméra Picamera2 sur Raspberry Pi 4 (AlphaBot2)

Ce guide t'explique comment calibrer la caméra du Raspberry Pi 4 à l'aide d'OpenCV et Picamera2, pour corriger la distorsion et améliorer la précision de la vision.

---

## ✅ 1. Préparation du système

### Installer les dépendances nécessaires

```bash
sudo apt update
sudo apt install python3-opencv python3-numpy python3-picamera2 --no-install-recommends
```

### Cloner le dépôt avec tout le nécessaire (scripts + damier)

```bash
git clone https://github.com/isc-bit-busters/RobotCameraCalibration.git
cd RobotCameraCalibration
```

---

## 🧩 2. Imprimer le damier de calibration

Le dépôt contient un fichier PDF à imprimer :

📄 [`Chessboard`](pattern.png)

- C'est un damier 9x6 (coins internes).
- Imprime-le **sans mise à l’échelle** sur une feuille A4.
- Colle-le sur un support rigide (carton, plaque, etc.).

---

## 📸 3. Capturer les images avec Picamera2

Dans le dépôt cloné, tu trouveras `capture_damier_picamera2.py`. Ce script te permet de capturer les images nécessaires à la calibration.

### Lancer la capture

```bash
python3 capture_damier_picamera2.py
```

### Contrôles

- Appuie sur **`c`** pour capturer une image contenant le damier.
- Appuie sur **Échap** pour quitter.

> ⚠️ Capture **entre 15 et 20 images** à différentes positions, inclinaisons et distances.

Les images sont automatiquement enregistrées dans le dossier `calibration_images/`.

---

✅ Une fois que tu as terminé la capture, passe à l'étape suivante :  
**4. Calibration avec OpenCV** (présente dans le dépôt sous `calibrer_camera.py`).


## Utilisation
Ajouter ces lignes tout au début du script
```python
calib = np.load("camera_calibration.npz")
camera_matrix = calib["camera_matrix"]
dist_coeffs = calib["dist_coeffs"]
FOCAL_LENGTH = camera_matrix[0, 0]
```

Si tu avais une valeur approximative de la focale, tu peux vérifier si elle correspond en utilisant le code suivant:
```python
# Afficher la valeur
print(f"Focale fx = {FOCAL_LENGTH:.2f} pixels")
```


