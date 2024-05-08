export default function loadBalancer(chinaDownload, USDownload) {
  // race method takes an array of promises and returns the promise that first settles
  return Promise.race([chinaDownload, USDownload]);
}
