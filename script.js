// 获取文章标题元素
const articleTitles = document.querySelectorAll('#article-list h2');

// 按标题排序的函数
function sortByTitle() {
  const sortedTitles = Array.from(articleTitles).sort((a, b) => a.textContent.localeCompare(b.textContent));
  const articleList = document.getElementById('article-list');
  const sortedList = document.createElement('div');
  sortedTitles.forEach(title => {
    sortedList.appendChild(title.parentNode);
  });
  articleList.parentNode.replaceChild(sortedList, articleList);
}

// 按发布时间排序的函数
function sortByPublishTime() {
  const sortedNodes = Array.from(articleTitles).sort((a, b) => {
    const timeA = new Date(a.dataset.publishTime);
    const timeB = new Date(b.dataset.publishTime);
    return timeA - timeB;
  });
  const articleList = document.getElementById('article-list');
  const sortedList = document.createElement('div');
  sortedNodes.forEach(node => {
    sortedList.appendChild(node.parentNode);
  });
  articleList.parentNode.replaceChild(sortedList, articleList);
}

// 给按钮添加点击事件
document.querySelector('button:first-child').addEventListener('click', sortByPublishTime);
document.querySelector('button:last-child').addEventListener('click', sortByTitle);