import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';
import { expect } from 'chai';

describe('createPushNotificationsJobs', () => {
  let queue;
  let jobData;
  let job;

  beforeEach(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
    jobData = {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    };
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('should create jobs in the queue', () => {
    createPushNotificationsJobs([jobData], queue);
    expect(queue.testMode.jobs.length).to.equal(1);
    job = queue.testMode.jobs[0];
    expect(job.type).to.equal('push_notification_code_3');
    expect(job.data).to.deep.equal(jobData);
  });

  it('should log Notification job created: JOB_ID when a job is created', () => {
    const consoleLogStub = chai.spy.on(console, 'log');
    createPushNotificationsJobs([jobData], queue);
    job = queue.testMode.jobs[0];
    expect(consoleLogStub).to.be.called.with.match(/^Notification job created: \d+$/);
  });

  it('should log Notification job JOB_ID completed when a job is complete', (done) => {
    createPushNotificationsJobs([jobData], queue);
    job = queue.testMode.jobs[0];
    job.on('complete', () => {
      const consoleLogStub = chai.spy.on(console, 'log');
      job.emit('complete');
      expect(consoleLogStub).to.be.called.with.match(/^Notification job \d+ completed$/);
      done();
    });
  });

  it('should log Notification job JOB_ID failed: ERROR when a job fails', (done) => {
    createPushNotificationsJobs([jobData], queue);
    job = queue.testMode.jobs[0];
    job.on('failed', () => {
      const consoleLogStub = chai.spy.on(console, 'log');
      job.emit('failed', new Error('Test failure'));
      expect(consoleLogStub).to.be.called.with.match(/^Notification job \d+ failed: Error: Test failure$/);
      done();
    });
  });

  it('should log Notification job JOB_ID PERCENT% complete when a job is in progress', (done) => {
    createPushNotificationsJobs([jobData], queue);
    job = queue.testMode.jobs[0];
    job.on('progress', (progress) => {
      const consoleLogStub = chai.spy.on(console, 'log');
      job.emit('progress', progress);
      expect(consoleLogStub).to.be.called.with.match(new RegExp(`^Notification job \\d+ ${progress}% complete$`));
      done();
    });
    job.emit('progress', 50);
  });
});
