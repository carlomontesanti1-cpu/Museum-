document.querySelectorAll('input[data-ba]').forEach(function(r){
  var box=r.parentElement, before=box.querySelectorAll('img')[1], marks=box.querySelectorAll('[data-ba-pos]');
  function set(){var v=Number(r.value); before.style.clipPath='inset(0 '+(100-v)+'% 0 0)'; marks.forEach(function(e){e.style.left=v+'%';});}
  r.addEventListener('input',set); set();
});
