const kue = require('kue');

const queue = kue.createQueue();

const jobData = {
  phoneNumber: "+2347015905170",
  message: "You are awesome, and weird!",
};


const job = queue.create('push_notification_code', jobData)
.save(function(err){
  if(!err) {
    console.log(`Notification job created: ${job.id}`);
  } else {
    console.error('Failed to create notification job:', err);
  }
});

job.on('complete', function() {
  console.log('Notification job completed');
  queue.shutdown(5000, (err) => {
    console.log('Kue shutdown:', err || 'No error');
    process.exit(0);
  });
});


job.on('failed', () => {
  console.log('Notification job failed');
  queue.shutdown(5000, (err) => {
    console.log('Kue shutdown:', err || 'No error');
    process.exit(1);
  });
});
