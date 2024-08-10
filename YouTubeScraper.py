function YoutubeScraper() {
  var spreadSheet = SpreadsheetApp.getActiveSpreadsheet();
  var activeSheet = spreadSheet.getActiveSheet();

  var searchTerms = ["Children Education", "Education Technology"];
  var results = [];
  var videoStats = [];

  searchTerms.forEach(function(term) {
    var search = YouTube.Search.list("snippet", {
      q: term,
      maxResults: 50
    });

    var searchResults = search.items.map(function(item) {
      return [item.id.videoId, item.snippet.title, item.snippet.publishedAt];
    });

    results = results.concat(searchResults);

    var ids = searchResults.map(function(id) {
      return id[0];
    }).join(",");

    var stats = YouTube.Videos.list("statistics", {
      id: ids
    });

    var statsResults = stats.items.map(function(item) {
      return [item.statistics.viewCount, item.statistics.likeCount, item.statistics.dislikeCount];
    });

    videoStats = videoStats.concat(statsResults);
  });

  activeSheet.getRange(2, 1, results.length, results[0].length).setValues(results);
  activeSheet.getRange(2, 4, videoStats.length, videoStats[0].length).setValues(videoStats);
}
