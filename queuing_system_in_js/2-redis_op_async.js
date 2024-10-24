import { createClient, print } from 'redis';
import { promisify } from 'util';

const redisClient = createClient();

// Make it to where .get method returns a promise for async functioning
const getAsync = promisify(redisClient.get).bind(redisClient);

redisClient.on('connect', () => {
    console.log('Redis client connected to the server');
});

redisClient.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
});

// Sets new key-value pair in Redis for school
const setNewSchool = (schoolName, value) => {
    redisClient.set(schoolName, value, print);
};

// Retrieves / displays value for a given school input (key)
const displaySchoolValue = async (schoolName) => {
    const value = await getAsync(schoolName);
    console.log(value);
};

(async () => {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
})();