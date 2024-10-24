import { createClient, print } from 'redis';

const redisClient = createClient();

// Listen for errors before connecting to client
redisClient.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
});

// Establish connection to Redis server
redisClient.connect().then(() => {
    console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
    redisClient.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
    redisClient.get(schoolName, (error, reply) => {
        console.log(reply);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');