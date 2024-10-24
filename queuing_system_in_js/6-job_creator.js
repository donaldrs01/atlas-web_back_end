import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
    phoneNumber: '555-123-1234',
    message: "This is a message that's being sent to your phone!",
};

// Creating a job in 'push_notification_code' queue
const job = queue.create('push_notification_code', jobData)
    .save((error) => {
        if (error) {
            console.error('Job creation failure');
        } else {
            console.log(`Notification job created: ${job.id}`);
        }
    });

job.on('complete', () => {
    console.log('Notification job completed');
});

job.on('failed', () => {
    console.log('Notification job failed');
});