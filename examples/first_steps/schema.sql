-- not much to explain here, but comments are always nice

CREATE TABLE product_inventory (
  product_id INTEGER PRIMARY KEY,
  label TEXT,
  count INTEGER,
  last_updated DATETIME DEFAULT CURRENT_TIMESTAMP
);
