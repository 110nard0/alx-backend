// 7-job_processor.js

import kue from 'kue';

const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100); // Track progress

  if (blacklistedNumbers.includes(phoneNumber)) {
    done(Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    job.progress(50, 100); // Update progress

    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done(); // Finish the job
  }
}

const queue = kue.createQueue({ concurrency: 2 }); // Process two jobs at a time

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
