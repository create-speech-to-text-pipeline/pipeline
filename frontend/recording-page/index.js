const fs = require('fs');
const multer = require('multer');

const storage = multer.diskStorage({
  destination(req, file, cb) {
    cb(null, 'uploads/');
  },
  filename(req, file, cb) {
    const fileNameArr = file.originalname.split('.');
    cb(null, `${Date.now()}.${fileNameArr[fileNameArr.length - 1]}`);
  },
});
const upload = multer({ storage });
const path = require('path');
const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.static('public/assets'));
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public/index.html'));
  });
app.use(express.static('uploads'));
app.post('/record', upload.single('audio'), (req, res) => res.json({ success: true }));
app.get('/recordings', (req, res) => {
    let files = fs.readdirSync(path.join(__dirname, 'uploads'));
    files = files.filter((file) => {
      // check that the files are audio files
      const fileNameArr = file.split('.');
      return fileNameArr[fileNameArr.length - 1] === 'mp3';
    }).map((file) => `/${file}`);
    return res.json({ success: true, files });
  });
app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`);
});