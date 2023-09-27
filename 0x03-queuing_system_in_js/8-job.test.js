// 8-job.test.js
import { createQueue } from 'kue';
import { describe, it, before, after, afterEach } from 'mocha';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';

const queue = createQueue();

describe('createPushNotificationsJobs', () => {
  beforeEach(() => {
    // Create a new queue before each test
    queue.testMode.enter();
  });

  afterEach(() => {
    // Clear the queue and exit test mode after each test
    queue.testMode.clear();
	queue.testMode.exit()
  });

  it('should display an error message if jobs is not an array', () => {
    // Call the function with a non-array argument and expect an error
    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs to the queue', () => {
    // Define a list of jobs
    const jobs = [
      { phoneNumber: '4153518780', message: 'Message 1' },
      { phoneNumber: '4153518781', message: 'Message 2' }
    ];

    // Call the function to create jobs
    createPushNotificationsJobs(jobs, queue);

    // Use queue.testMode.jobs to get the list of jobs in the queue
    const queueJobs = queue.testMode.jobs;

    // Check if the jobs were added to the queue
    expect(queueJobs.length).to.equal(2);

    // Check if the jobs have the correct data
    expect(queueJobs[0].type).to.equal('push_notification_code_3');
    expect(queueJobs[0].data.phoneNumber).to.equal('4153518780');
    expect(queueJobs[0].data.message).to.equal('Message 1');

    expect(queueJobs[1].type).to.equal('push_notification_code_3');
    expect(queueJobs[1].data.phoneNumber).to.equal('4153518781');
    expect(queueJobs[1].data.message).to.equal('Message 2');
  });
});
