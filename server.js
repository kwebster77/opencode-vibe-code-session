const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());
app.use(express.static('.'));

const db = new sqlite3.Database('books.db');

db.serialize(() => {
    db.run('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, created_at DATETIME DEFAULT CURRENT_TIMESTAMP)');
});

app.post('/add', (req, res) => {
    const { bookName } = req.body;
    
    if (!bookName) {
        return res.status(400).json({ error: 'Book name is required' });
    }
    
    db.run('INSERT INTO books (name) VALUES (?)', [bookName], function(err) {
        if (err) {
            return res.status(500).json({ error: 'Database error' });
        }
        
        res.json({ 
            id: this.lastID, 
            name: bookName, 
            message: 'Book added successfully' 
        });
    });
});

app.get('/books', (req, res) => {
    db.all('SELECT * FROM books ORDER BY created_at DESC', (err, rows) => {
        if (err) {
            return res.status(500).json({ error: 'Database error' });
        }
        res.json(rows);
    });
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});