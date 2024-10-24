import { createClient, print } from 'redis';

const redisClient = createClient();

redisClient.on('connect', () => {
    console.log('Redis client connected to the server');
});

redisClient.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
});

// Store values in HolbertonSchools hash
redisClient.hSet('HolbertonSchools', 'Portland', 50, print);
redisClient.hSet('HolbertonSchools', 'Seattle', 80, print);
redisClient.hSet('HolbertonSchools', 'New York', 20, print);
redisClient.hSet('HolbertonSchools', 'Bogota', 20, print);
redisClient.hSet('HolbertonSchools', 'Cali', 40, print);
redisClient.hSet('HolbertonSchools', 'Paris', 2, print);

// hgetall to display all stored hashes
redisClient.hGetAll('HolbertonSchools').then((result) => {
    console.log(result);
    redisClient.quit(); // close connection
});




