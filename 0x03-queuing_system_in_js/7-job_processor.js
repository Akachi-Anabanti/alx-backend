// job processor
const kue = require('kue');

const blacklist = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
  if (blacklist.includes(phoneNumber)) {
    // track the progress
    job.progress(0, 100);
    
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // set the progress to 50%
  job.progress(50, 100);

  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

const queue = kue.createQueue();

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
