new Vue({
    el:"#results",
    data:{
          message:[],
        },
    methods:{
        showResults(){
            var self = this;
            axios.get('/extra')
            .then(function (response) {
                self.message = [];
                for(let item of response.data) {
                    self.message.push(item);
                }
            })
        }
      }
});
new Vue({
    el:"#extra",
    data:{
        ext:{
            id:'',
            name:'',
        },
        exts: [{
                id:'SE112',
                name:'软件工程职业素养',
            }, {
                id:'SE418',
                name:'软件产品设计与用户体验',
            }, {
                id:'SE419',
                name:'企业软件质量保证',
            }, {
                id:'SE420',
                name:'软件知识产权保护',
            }, {
                id:'SE422',
                name:'企业软件过程与管理',
            }, {
                id:'SE417',
                name:'软件工程经济学',
            }, {
                id:'SE315',
                name:'操作系统',
            }, {
                id:'EI901',
                name:'工程实践与科技创新',
            }]
    },
    methods:{
        addExt:function(){
            this.exts.push(this.ext);
            this.ext = {
                        id:'',
                        name:'',
                    };
            axios.post('/extra', 
                        JSON.stringify(this.exts)
                      )
                      .then(function (response) {
                        console.log(response);
                      })
        },
        delExt:function(index){
            var index = this.exts.findIndex(function(item){
                    return item.id == index;
                });
                this.exts.splice(index,1);
            axios.post('/extra', 
                        JSON.stringify(this.exts)
                      )
                      .then(function (response) {
                        console.log(response);
                      })
        },
    }
});