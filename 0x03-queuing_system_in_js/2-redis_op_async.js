// redis
import { createClient, print} from 'redis';
import { promisify } from 'util';


const client = createClient();

client .on('error', err => console.log('Redis client not connected to the server:', err));

client.on('connect', () => {
    console.log('Redis client connected to the server')
});

const getAsync = promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
};


async function displaySchoolValue(schoolName) {
  try {
    const reply = await getAsync(schoolName);
    console.log(reply);
  } catch (error) {
    console.error('Error getting value:'. error);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
