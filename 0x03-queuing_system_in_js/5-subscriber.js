// 5-subscriber.js

import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
  client.subscribe('holberton school channel');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

client.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});

/* const subscription = redis.createClient();

subscription.on('connect', () => {
  console.log('Subscriber connected to the server');
  subscription.subscribe('holberton school channel');
});

subscription.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    subscription.unsubscribe();
    subscription.quit();
    client.quit();
  }
});
*/
