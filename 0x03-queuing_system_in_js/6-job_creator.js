// 6-job_creator.js

import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a test message.'
};

const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

queue.on('job complete', (id) => {
  kue.Job.get(id, (err, job) => {
    if (err) throw err;
    console.log('Notification job completed');
    job.remove((err) => {
      if (err) throw err;
      console.log(`Removed completed job #${job.id}`);
      queue.shutdown(5000, (err) => {
        console.log('Kue shutdown: ', err || 'OK');
        process.exit(0);
      });
    });
  });
});

queue.on('job failed', (id, result) => {
  console.log(`Notification job failed with result ${result}`);
});
