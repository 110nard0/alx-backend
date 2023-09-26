import { createClient, print } from 'redis';
import { promisify } from 'util'

const client = createClient()
  .on('connect', () => {
    console.log('Redis client connected to the server')
  })
  .on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

async function setNewSchool(schoolName, value) {
  await setAsync(schoolName, value);
  console.log('Reply: OK');
}

async function displaySchoolValue(schoolName) {
  const value = await getAsync(schoolName);
  console.log(value);
}

async function main() {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

main();
