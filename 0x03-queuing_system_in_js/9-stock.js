import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const client = redis.createClient();

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const products = [
  { itemId: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { itemId: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { itemId: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { itemId: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

let listProducts = products.map(product => {
	product.initialAvailableQuantity = product.stock;
	product.currentQuantity = product.stock;
	delete product.stock;
	return product;
});

// Data access
const getItemById = (id) => listProducts.find(item => item.itemId === id);

// In stock in Redis
const reserveStockById = async (itemId, stock) => {
  await setAsync(`item.${itemId}`, stock);
};

const getCurrentReservedStockById = async (itemId) => {
  const reservedStock = await getAsync(`item.${itemId}`);
  return reservedStock ? parseInt(reservedStock) : getItemById(itemId).currentQuantity;
};

// Routes
app.get('/list_products', (req, res) => {
  const returnList = listProducts.map(product => {
	let {currentQuantity, ...withoutCurrentQuantity} = product;
	return withoutCurrentQuantity;
  });
  res.json(returnList);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (item) {
    const currentQuantity = await getCurrentReservedStockById(itemId);
    const response = {
      ...item,
      currentQuantity
    };
    res.json(response);
  } else {
    res.json({ status: 'Product not found' });
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (item) {
    const currentQuantity = await getCurrentReservedStockById(itemId);

    if (currentQuantity > 0) {
      await reserveStockById(itemId, currentQuantity - 1);
      res.json({ status: 'Reservation confirmed', itemId });
    } else {
      res.json({ status: 'Not enough stock available', itemId });
    }
  } else {
    res.json({ status: 'Product not found' });
  }
});

// Start server
const PORT = 1245;

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
