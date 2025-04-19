const express = require('express');
const { Pool } = require('pg');
const app = express();
app.use(express.json());

const pool = new Pool({
  host: process.env.DB_HOST,
  port: process.env.DB_PORT,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
});

app.post('/orders', async (req, res) => {
  const { user_id, product } = req.body;
  try {
    const result = await pool.query(
      'INSERT INTO orders(user_id, product) VALUES($1, $2) RETURNING id',
      [user_id, product]
    );
    res.json({ id: result.rows[0].id });
  } catch (err) {
    console.error(err);
    res.status(500).send('Error inserting order');
  }
});

app.listen(3000, () => console.log('Order service listening on port 3000'));