var num = 0;
(function (d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s);
  js.id = id;
  js.src = "https://vk.com/js/api/openapi.js?157";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'vk_openapi_js'));
(function () {
  if (!window.VK || !VK.Widgets || !VK.Widgets.Post || !VK.Widgets.Post('vk_post_-2473_17675', -2473, 17675, 'TbxfrljpjmXPCMLrJZEv9A6VXoUc')) setTimeout(arguments.callee, 50);
}());

(function () {
  var chat = {
    messageToSend: '',
    messageResponses: [
      'Why did the web developer leave the restaurant? Because of the table layout.',
      'How do you comfort a JavaScript bug? You console it.',
      'An SQL query enters a bar, approaches two tables and asks: "May I join you?"',
      'What is the most used language in programming? Profanity.',
      'What is the object-oriented way to become wealthy? Inheritance.',
      'An SEO expert walks into a bar, bars, pub, tavern, public house, Irish pub, drinks, beer, alcohol'
    ],
    init: function () {
      this.cacheDOM();
      this.bindEvents();
      this.render();
    },
    cacheDOM: function () {
      this.$chatHistory = $('.chat-history');
      this.$button = $('button');
      this.$textarea = $('#message-to-send');
      this.$chatHistoryList = this.$chatHistory.find('ul');
    },
    bindEvents: function () {
      this.$button.on('click', this.addMessage.bind(this));
      this.$textarea.on('keyup', this.addMessageEnter.bind(this));
    },
    render: function (hash, g_i, p_i) {
      this.scrollToBottom();
      if (this.messageToSend.trim() !== '') {
        var template = Handlebars.compile($("#message-template").html());
        var context = {
          messageOutput: this.messageToSend,
          time: this.getCurrentTime()
        };

        this.$chatHistoryList.append('<li class="clearfix animated bounceInRight delay-1"><div class="message-data align-right"><span class="message-data-time">Today</span> &nbsp; &nbsp;<span class="message-data-name">Вы</span><i class="fa fa-circle me"></i></div><div class="message other-message float-right">' + this.messageToSend + '</div></li>');
        this.scrollToBottom();
        this.$textarea.val('');

        // responses
        var templateResponse = Handlebars.compile($("#message-response-template").html());
        var contextResponse = {
          response: this.send_to_server(this.messageToSend),
          time: this.getCurrentTime()
        };

        setTimeout(function () {
         // this.$chatHistoryList.append('');
          this.scrollToBottom();
        }.bind(this), 1500);

      }

    },

    addMessage: function () {
      this.messageToSend = this.$textarea.val()
      this.render();
    },
    addMessageEnter: function (event) {
      // enter was pressed
      if (event.keyCode === 13) {
        this.addMessage();
      }
    },
    scrollToBottom: function () {
      this.$chatHistory.scrollTop(this.$chatHistory[0].scrollHeight);
    },
    getCurrentTime: function () {
      return new Date().toLocaleTimeString().
      replace(/([\d]+:[\d]{2})(:[\d]{2})(.*)/, "$1$3");
    },
    getRandomItem: function (arr) {
      return arr[Math.floor(Math.random() * arr.length)];
    },
    send_to_server: function (mes) {
      var res = '';

      $.ajax({
        type: "POST",
        url: "/api/addres",
        data: {
          msg: mes
        },
        success: function (result) {

          res = result;
          list_of_text = res.split('~!~');
          hash = list_of_text[0];
          g_i = list_of_text[1];
          p_i = list_of_text[2];
          proc_text = list_of_text[3]
          variority  = list_of_text[4]
          p_i = p_i.replace(/\s/g, '')
          console.log(p_i);
          this.$chatHistory = $('.chat-history');
          this.$button = $('button');
          this.$textarea = $('#message-to-send');
          this.$chatHistoryList = this.$chatHistory.find('ul');
          num+=1;
          post_id = "vk_post"+'_-'+num+'_'+p_i;
          console.log(post_id)
          //this.$chatHistoryList.append('<li class="animated bounceInLeft delay-2"> <div class="message-data"> <span class="message-data-name"><i class="fa fa-circle online"></i> Vincent</span> <span class="message-data-time">Today</span> </div> <div class="message my-message ">' + proc_text + '</div> </li>')
          this.$chatHistoryList.append('<li class="animated bounceInLeft delay-1> <div class="message-data"> <span class="message-data-name"><i class="fa fa-circle online"></i> Vincent</span> <span class="message-data-time"></span> </div> <div class="message my-message">' + variority + '</div> </li>')
          this.$chatHistoryList.append('<li class="animated bounceInLeft delay-2> <div class="message-data"> <span class="message-data-name"><i class="fa fa-circle online"></i> Vincent</span> <span class="message-data-time"></span> </div> <div class="message my-message">W2V-релевантный пост:<div id="'+post_id+'"></div> <script type="text/javascript"> (function(d, s, id) { var js, fjs = d.getElementsByTagName(s)[0]; if (d.getElementById(id)) return; js = d.createElement(s); js.id = id; js.src = "https://vk.com/js/api/openapi.js?157"; fjs.parentNode.insertBefore(js, fjs); }(document, "script", "vk_openapi_js")); (function() { if (!window.VK || !VK.Widgets || !VK.Widgets.Post || !VK.Widgets.Post("'+post_id+'", -'+g_i+', '+p_i+', "'+hash+'")) setTimeout(arguments.callee, 50); }()); </script></div> </li>');
          this.$chatHistory.scrollTop(this.$chatHistory[0].scrollHeight);
        }
      });

    }

  };

  chat.init();
})();
